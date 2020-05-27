#!/usr/bin/env python
from setuptools import setup
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(name='hotmart-python',
      version='0.1',
      description='Hotmart Hotconnect requests made easy',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='Bruno Armanelli',
      author_email='brunoarmanelli@me.com',
      url='https://github.com/brunoarmanelli/hotmart-python',
      packages=['hotconnect'],
      keywords='hotmart hotconnect',
      install_requires=['requests', 'six']
     )