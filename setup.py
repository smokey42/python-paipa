from setuptools import setup

try:
    from os.path import abspath, dirname, join
    _desc = join(dirname(abspath(__file__)), 'README.rst')
    long_description = open(_desc, 'r').read()
except IOError:
    long_description = "python-paipa"


setup(
    name='paipa',
    version='0.1.1',
    description='Python pipeline library. Maori: (noun) pipe.',
    long_description=long_description,
    packages=['paipa'],
    author='python-paipa contributors',
    author_email='python-tribe@stylight.com',
    url='https://github.com/stylight/python-paipa',
    license='Apache Software License 2.0',
    tests_require=[
        'tox',
    ],
    install_requires=[
        'six',
        'enum34',
    ],
    extras_require={
        'glue': ['tornado'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
