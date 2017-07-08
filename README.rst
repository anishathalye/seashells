Seashells
=========

The official client for `Seashells.io <https://seashells.io>`__.

Installation
------------

Seashells is compatible with both Python 2 and Python 3. It's recommended that
you use Python 3.

You can install Seashells from
`PyPI <https://pypi.python.org/pypi/seashells/>`__:

.. code:: bash

    pip install seashells

Usage
-----

See the instructions on `Seashells.io <https://seashells.io>`__ for more
information about Seashells. For more information on how to use the command
line tool itself, see the built-in help:

.. code:: bash

    seashells --help

Packaging
---------

1. Update version information.

2. Build the package using ``python3 setup.py sdist bdist_wheel``.

3. Sign and upload the package using ``twine upload -s dist/*``.

License
-------

Copyright (c) 2017 Anish Athalye. Released under the MIT License. See
`LICENSE.rst <LICENSE.rst>`__ for details.
