from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='forbiddenfluent',
    version='0.1',
    url="https://github.com/nickdelgrosso/forbiddenfluent",
    author="Nicholas A. Del Grosso",
    author_email="delgrosso.nick@gmail.com",
    description="Adds iteration methods like zip, filter, apply to built-in Python collections in a fluent programming style.",
    #long_description="This module adds the built-in functions that work on iterables and make them into methods in order to support a fluent programming style.",
    packages=find_packages(),
    license='GNU General Public License, Version 3',
    classifiers=[
        "Programming Language :: Python :: 3",
        ],
    python_requires='>=3.6',
)
