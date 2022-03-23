#! /usr/bin/env python3

from setuptools import setup, find_packages

requires = [
    'requests',
    'aiohttp < 4.0.0',
    'Sphinx',
    'sphinx_rtd_theme',
]

setup(
    name="aosm2m",
    version="0.0.1",
    #packages=['aosm2m'],
    packages=find_packages(),
    install_requires=requires
)
