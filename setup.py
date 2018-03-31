#!/usr/bin/env python

from setuptools import setup, find_packages


# parse version string from the __init__ file
with open("records/__init__.py", "r") as initfile:
    lines = initfile.readlines()
    for line in lines:
        if "__version__" in line:
            # get version line and strip white space and quotations
            version = line.strip().split()[-1].strip("'").strip('"')


# build command
setup(
    name="records",
    version=version,
    packages=find_packages(),
    author="Neha Savant",
    author_email="ngs2116@columbia.edu",
    license="GPLv3",
    description="A package for querying GBIF",
    classifiers=["Programming Language :: Python :: 3"],
)