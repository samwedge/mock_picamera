from setuptools import setup, find_packages
from os import path
import picamera

here = path.abspath(path.dirname(__file__))

setup(
    name='picamera',

    version=picamera.__version__,

    description='A mock Raspberry Pi picamera library for developing code before deploying to a Pi',

    url='https://github.com/samwedge/mock_picamera',

    author='Sam Wedge',
    author_email='samwedge@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='raspberry pi raspi picamera camera mock dummy fake test testing',

    packages=find_packages(exclude=[]),

    install_requires=[],

    extras_require={},

    package_data={},

    data_files=[],

    entry_points={}
)
