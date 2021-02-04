
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='str2port',
    version='0.1.1',
    description='Convert string to md5 hash, then to port number. No randomization involved.',
    project_urls={
        "homepage": "https://github.com/kritarthh/str2port", "repository": "https://github.com/kritarthh/str2port"},
    author='Pacharapol Withayasakpunt',
    author_email='patarapolw@gmail.com',
    license='MIT',
    entry_points={"console_scripts": ["str2port = str2port.__main__:cli"]},
    packages=['str2port'],
    package_dir={"": "."},
    package_data={"str2port": ["*.csv"]},
    install_requires=['click==7.*,>=7.0.0'],
)
