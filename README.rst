Seashells
=========

The official client for `Seashells.io <https://seashells.io>`__.

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

See the instructions on `Seashells.io <https://seashells.io>`__ for more
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

Packaging
---------

1. Update version information.

2. Build the package using ``python3 setup.py sdist bdist_wheel``.

3. Sign and upload the package using ``twine upload -s dist/*``.

License
-------

Copyright (c) 2018 Anish Athalye. Released under the MIT License. See
`LICENSE.rst <LICENSE.rst>`__ for details.
