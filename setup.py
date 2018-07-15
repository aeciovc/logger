from setuptools import setup, find_packages

import os

README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='logger',
    version='0.0.1',
    description='Logger is a module to provide default log setup and others kind of log systems',
    long_description=open(README).read(),
    license='MIT',
    packages=find_packages(exclude=['test', 'test.*']),
    author='Aécio Costa',
    author_email='aeciovc@gmail.com',
    keywords=['log'],
    url='https://github.com/aeciovc/logger.git',
    include_package_data=True
)