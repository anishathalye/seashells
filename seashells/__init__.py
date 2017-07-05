#!/usr/bin/env python

# Copyright (c) 2017 Anish Athalye (me@anishathalye.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import socket
import sys
import os
import select
import time

__version__ = '0.1.0'


SERVER_IP = 'seashells.io'
SERVER_PORT = 1337
RECV_BUFFER_SIZE = 1024
READ_BUFFER_SIZE = 1024
SOCKET_TIMEOUT = 10 # seconds


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quiet', action='store_true',
            help='disable stdin passthrough')
    parser.add_argument('-i', '--ip', default=SERVER_IP,
            help='server IP address')
    parser.add_argument('-p', '--port', default=SERVER_PORT,
            help='server port')
    parser.add_argument('-d', '--delay', type=float, default=0,
            help='delay before starting to send data')
    return parser


def main():
    source = sys.stdin.buffer
    try:
        parser = make_parser()
        args = parser.parse_args()

        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(SOCKET_TIMEOUT)
        conn.connect((args.ip, args.port))

        # get URL from server first
        conn.settimeout(SOCKET_TIMEOUT)
        data = conn.recv(RECV_BUFFER_SIZE)
        sys.stderr.buffer.write(data)
        sys.stderr.flush()

        time.sleep(args.delay)

        # pipe data from stdin to server
        while True:
            ready, _, _ = select.select([conn, source], [], [])
            if conn in ready:
                conn.settimeout(SOCKET_TIMEOUT)
                data = conn.recv(RECV_BUFFER_SIZE)
                sys.stderr.buffer.write(data)
                sys.stderr.flush()
            elif source in ready:
                inp = source.read1(READ_BUFFER_SIZE)
                if len(inp) == 0:
                    # EOF
                    break
                conn.sendall(inp)
                if not args.quiet:
                    sys.stdout.buffer.write(inp)
                    sys.stdout.flush()
    except KeyboardInterrupt:
        # exit silently with an error code
        exit(1)
    except socket.error as e:
        sys.stderr.write('socket error: %s\n' % e)
        sys.stderr.flush()
        # continue running
        while True:
            try:
                inp = source.read1(READ_BUFFER_SIZE)
                if len(inp) == 0:
                    # EOF
                    break
                if not args.quiet:
                    sys.stdout.buffer.write(inp)
                    sys.stdout.flush()
            except KeyboardInterrupt:
                exit(1)


if __name__ == '__main__':
    main()
