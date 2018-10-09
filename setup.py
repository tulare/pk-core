# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

# Get version without import module
exec(compile(open('pk_core/version.py').read(),
             'pk_core/version.py', 'exec'))

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies
]

with open('README.md') as f :
    readme = f.read()

with open('LICENSE') as f :
    license = f.read()

setup(
    name='pk-core',
    version=__version__,
    description='Core utils for python projects',
    long_description=readme,
    author='Tulare Regnus',
    author_email='tulare.paxgalactica@gmail.com',
    url='https://github.com/tulare/pk-core',
    license=license,
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    install_requires=install_requires
)
