Seashells
=========

The official client for `seashells.io <https://seashells.io>`__.

The server code is available at `anishathalye/seashells-server
<https://github.com/anishathalye/seashells-server>`__.

For more information, see `seashells.io <https://seashells.io>`__ or the
`launch blog post <https://www.anishathalye.com/2017/07/10/seashells/>`__.

Installation
------------

Seashells is compatible with both Python 2 and Python 3. It's recommended that
you use Python 3.

You can install Seashells from
`PyPI <https://pypi.org/project/seashells/>`__:

.. code:: bash

    pip install seashells

Usage
-----

See the instructions on `seashells.io <https://seashells.io>`__ for more
information about Seashells. For more information on how to use the command
line tool itself, see the built-in help:

.. code:: bash

    seashells --help

Tips and Tricks
~~~~~~~~~~~~~~~

- To easily pipe both stdout and stderr to seashells, you can set up a shell
  function (`source
  <https://github.com/anishathalye/seashells/issues/14#issuecomment-409167113>`__):

  .. code:: bash

     function sea() {
         $* 2>&1 | seashells
     }

Other Clients
-------------

- `roccomuso/seashells <https://github.com/roccomuso/seashells>`__ (Node.js)
- `hans-strudle/seashells <https://github.com/hans-strudle/seashells>`__ (Go)

Note: other clients are not officially supported.

License
-------

Copyright (c) Anish Athalye. Released under the MIT License. See
`LICENSE.rst <LICENSE.rst>`__ for details.
