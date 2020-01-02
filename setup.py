from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='forbiddenfluent',
    version='0.1',
    author="Nicholas A. Del Grosso",
    author_email="delgrosso.nick@gmail.com",
    description="Adds iteration methods like zip, filter, apply to built-in Python collections in a fluent programming style.",
    long_description=Path("README.md").read_text()
    packages=find_packages(),
    license='GNU General Public License, Version 3',
)
