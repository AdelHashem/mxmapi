from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mxmapi",
    version="0.1.2",
    description="A simple Python library for the Musixmatch Web API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mxmapi.readthedocs.io/",
    author="Adel Hashem",
    author_email="adel.mohamed.9998@gmail.com",
    license="MIT",
    project_urls={
        'Source': 'https://github.com/AdelHashem/mxmapi',
    },
    packages=["mxmapi"],
    include_package_data=True,
    install_requires=[
        "requests>=2.25.0",
        "urllib3>=1.26.0"
    ]
)