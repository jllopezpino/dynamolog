# -*- coding: utf-8 *-*
try:
    from setuptools import setup
except ImportError:
    from distutils import setup


long_description = open("README.rst").read()

setup(
    name='dynamolog',
    version='0.1.1',
    description='Python centralized logging using DynamoDB',
    long_description=long_description,
    author='Jose Luis Lopez Pino',
    author_email='jllopezpino@gmail.com',
    maintainer='Jose Luis Lopez Pino',
    maintainer_email="jllopezpino@gmail.com",
    url='https://github.com/jllopezpino/dynamolog',
    download_url = 'https://github.com/jllopezpino/dynamolog/tarball/0.1.1',
    packages=['dynamolog'],
    keywords=["dynamolog", "logging", "dynamo", "dynamodb"],
    install_requires=['boto'],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: System :: Logging",
        "Topic :: Database"],
)
