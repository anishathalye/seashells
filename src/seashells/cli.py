import argparse
import os
import select
import socket
import sys
import time

SERVER_IP = "seashells.io"
SERVER_PORT = 1337
RECV_BUFFER_SIZE = 1024
READ_BUFFER_SIZE = 1024
SOCKET_TIMEOUT = 10  # seconds


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--quiet", action="store_true", help="disable stdin passthrough")
    parser.add_argument("-i", "--ip", default=SERVER_IP, help="server IP address")
    parser.add_argument("-p", "--port", type=int, default=SERVER_PORT, help="server port")
    parser.add_argument("-d", "--delay", type=float, default=0, help="delay before starting to send data")
    return parser


def read1(stream):
    if hasattr(stream, "read1"):
        return stream.read1(READ_BUFFER_SIZE)
    # XXX: is there a better way to do this without doing a bunch of syscalls?
    buf = []
    while len(buf) < READ_BUFFER_SIZE:
        ready, _, _ = select.select([stream], [], [], 0)  # poll
        if not ready:
            break
        data = stream.read(1)
        if not data:
            # even if we hit this case, it's fine: once we get to EOF, the
            # fd is always ready (and will always return "")
            break
        buf.append(data)
    return "".join(buf)


def main():
    stdin = sys.stdin.buffer if hasattr(sys.stdin, "buffer") else os.fdopen(sys.stdin.fileno(), "r", 0)
    stdout = sys.stdout.buffer if hasattr(sys.stdout, "buffer") else sys.stdout
    stderr = sys.stderr.buffer if hasattr(sys.stderr, "buffer") else sys.stderr

    try:
        parser = make_parser()
        args = parser.parse_args()

        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(SOCKET_TIMEOUT)
        conn.connect((args.ip, args.port))

        # get URL from server first
        conn.settimeout(SOCKET_TIMEOUT)
        data = conn.recv(RECV_BUFFER_SIZE)
        stderr.write(data)
        stderr.flush()

        time.sleep(args.delay)

        # pipe data from stdin to server
        while True:
            ready, _, _ = select.select([conn, stdin], [], [])
            if conn in ready:
                conn.settimeout(SOCKET_TIMEOUT)
                data = conn.recv(RECV_BUFFER_SIZE)
                stderr.write(data)
                stderr.flush()
            elif stdin in ready:
                inp = read1(stdin)
                if len(inp) == 0:
                    # EOF
                    break
                conn.sendall(inp)
                if not args.quiet:
                    stdout.write(inp)
                    stdout.flush()
    except KeyboardInterrupt:
        # exit silently with an error code
        sys.exit(1)
    except OSError as e:
        stderr.write(f"socket error: {e}\n".encode())
        stderr.flush()
        # continue running
        while True:
            try:
                inp = read1(stdin)
                if len(inp) == 0:
                    # EOF
                    break
                if not args.quiet:
                    stdout.write(inp)
                    stdout.flush()
            except KeyboardInterrupt:
                sys.exit(1)
