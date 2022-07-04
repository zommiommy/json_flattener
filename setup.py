import os
import re
# To use a consistent encoding
from codecs import open as copen

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with copen(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def read(*parts):
    with copen(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("json_flattener", "__version__.py")

test_deps =[
    "pytest",
]

setup(
    name='json_flattener',
    version=__version__,
    description="a python package to flatten a JSON into a list of strings and back",
    long_description=long_description,
    url="https://github.com/zommiommy/json_flattener",
    author="Tommaso Fontana",
    author_email="tommaso.fontana.96@gmail.com",
    # Choose your license
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    # Add here the package dependencies
    install_requires=[],
)