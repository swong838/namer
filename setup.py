import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

with open(f'{here}/requirements.txt') as reqs:
    requirements = [req.strip() for req in reqs if not req.startswith('#')]

with open(f'{here}/test-requirements.txt') as reqs:
    test_requirements = [req.strip() for req in reqs if not req.startswith('#')]

setup(
    name='Namer',
    version='0.1.0',
    description='File renamer by directory',
    setup_requires=['setuptools-git'],
    install_requires=requirements,
    tests_require=test_requirements,
)
