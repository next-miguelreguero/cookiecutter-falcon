# -*- coding: utf-8 -*-
import os

import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "requirements", "requirements.txt"), 'r') as f:
    install_req = f.readlines()

with open(os.path.join(HERE, "requirements", "test-requirements.txt"), 'r') as f:
    test_req = f.readlines()


setuptools.setup(
    name='{{cookiecutter.project_name}}',
    description='{{cookiecutter.project_description}}',
    version=':versiontools:{{cookiecutter.project_slug}}:',

    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=install_req,
    tests_require=test_req,
    setup_requires=('versiontools'),

    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_mail}}',
    url='{{cookiecutter.project_url}}',
)
