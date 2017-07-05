from setuptools import setup
from codecs import open # For a consistent encoding
from os import path
import re


here = path.dirname(__file__)


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def read(*names, **kwargs):
    with open(
        path.join(here, *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='seashells',

    version=find_version('seashells', '__init__.py'),

    description='The official client for Seashells.io',
    long_description=long_description,

    url='https://github.com/anishathalye/seashells',

    author='Anish Athalye',
    author_email='me@anishathalye.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='shell',

    packages=['seashells'],

    install_requires=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'seashells=seashells:main',
        ],
    },
)
