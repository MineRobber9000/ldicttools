#!/usr/bin/env python

from setuptools import setup

with open("README.rst") as readme:
    long_description = readme.read()

install_requires = []

with open("requirements.txt") as req:
	install_requires = [line.strip() for line in req.readlines()]

setup(
    name='directory',
    version='0.1.0',
    description='Tools for searching/indexing directories',
    long_description=long_description,
    author='Robert Miles',
    author_email='milesrobert374@gmail.com',
    url='https://github.com/MineRobber9000/directory',
    keywords='novelty-calendars',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['directory'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [],
    }
)
