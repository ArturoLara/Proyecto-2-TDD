# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='Practica 2 TDD',
    version='1.0.0',
    description='Practica para contar el numero de palabras que aparecen en un texto',
    long_description=readme,
    author='Alfonso Cuesta y Arturo Lara',
    packages=find_packages(exclude=('tests', 'docs'))
)