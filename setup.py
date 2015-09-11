import os
if os.getenv('VBOX_MOUNTED'):

    del os.link

from setuptools import setup
from setuptools import find_packages


with open('README.rst', 'r') as readmefile:

    README = readmefile.read()

setup(
    name='Portal',
    version='0.1.0',
    url='<URL>',
    description='<TAGLINE>',
    long_description=README,
    packages=find_packages(exclude=['tests', 'build', 'dist', 'docs']),
    install_requires=[
        'six',
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'Portal-run = Flask_Project.run:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)