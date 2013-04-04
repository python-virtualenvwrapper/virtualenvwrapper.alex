#!/usr/bin/env python

PROJECT = 'virtualenvwrapper.alex'
VERSION = '0.1'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

try:
    long_description = open('README', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='virtualenvwrapper plugin to alias common typos',
    long_description=long_description,

    author='Doug Hellmann',
    author_email='doug.hellmann@gmail.com',

    url='https://bitbucket.org/dhellmann/virtualenvwrapper.alex',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],

    platforms=['Any'],

    provides=['virtualenvwrapper.alex',
              ],
    requires=['virtualenv',
              'virtualenvwrapper (>=2.9)',
              ],

    namespace_packages=['virtualenvwrapper'],
    packages=['virtualenvwrapper'],
    include_package_data=True,

    entry_points={
        'virtualenvwrapper.initialize_source': [
            'alex = virtualenvwrapper.alex:initialize_source',
        ],
    },

    zip_safe=False,
)
