# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bigbluebutton/__init__.py
from bigbluebutton import __version__ as version

setup(
	name='bigbluebutton',
	version=version,
	description='A BBB plugin for ERPNext to schedule and join meeting',
	author='Sanjay Kumar',
	author_email='sanjay.kumar001@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
