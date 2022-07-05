# Standard library imports
from os import path

# Third party imports
from setuptools import (  # Always prefer setuptools over distutils
    find_packages,
    setup,
)

here = path.abspath(path.dirname(__file__))

setup(
    name="toolbox6",
    version="0.0.1",
    description="It is a toolbox to day to day working with python(async or not) for data pipelines or API's.",
    long_description="",
    url="https://github.com/sixcodes/toolbox6",
    # Author details
    author="Jesué Junior",
    author_email="opensource@sixcodes.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    # TODO: Implement the aditional package to be installed. E.g: toolbox6[gcp], toolbox6[aws]
    install_requires=[
        "pydantic>=1.7.2",
        "pyarrow>=2.0.0",
        "aioredis>=1.3.0",
        "numpy>=1.0.0",
        "pandas>=1.0.0,<=1.1.4>",
        "crcmod>=1.7",
        "google-cloud-pubsub>=2.2.0",
        "google-cloud-bigquery>=1.24.0",
        "google-cloud-storage>=1.29.0",
        "gcsfs>=0.7.1",
        "structlog>=20.1.0",
        # "boto3>=1.14.63",
        # "s3fs>=0.5.1",
        "ujson==5.4.0",
    ],
    entry_points={},
)
