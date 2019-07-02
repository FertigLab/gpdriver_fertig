import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*\'(.*)\'',
    open('gpdriver_fertig/_version.py').read(),
    re.M
    ).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name='gpdriver_fertig',
    version='0.0.1',
    packages=['gpdriver_fertig'],
    description='Package for managing environments and notebooks on genepattern.org',
    long_description=long_descr,
    url='https://github.com/FertigLab/gpdriver_fertig',
)

