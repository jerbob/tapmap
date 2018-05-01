"""TapMap: A generator for keyboard heatmap images."""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='tapmap',
    version='1.2',
    description='A generator for keyboard heatmap images',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AnonGuy/TapMap',
    author='Jeremiah Boby',
    author_email='jeremiahboby@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    py_modules=['tapmap.char_map', 'tapmap.processing'],
    keywords='matplotlib PIL numpy',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['Pillow', 'numpy', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'tapmap=tapmap:main',
        ],
    },
    include_package_data=True
)
