from setuptools import setup

def readme() :
    with open('README.md') as f :
        return f.read()

def license() :
    with open('LICENSE') as f:
        return f.read()

# Get version without import module
with open('src/pk_core/version.py') as f :
    exec(compile(f.read(), 'pk_core/version.py', 'exec'))

setup(
    name='pk-core',
    version=__version__,
    description='Core utils for python projects',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Topic :: Utilities :: Core',
    ],
    keywords='python utilities core',
    url='https://github.com/tulare/pk-core',
    author='Tulare Regnus',
    author_email='tulare.paxgalactica@gmail.com',
    license=license(),
    package_dir={'pk_core' : 'src/pk_core'},
    packages=['pk_core'],
    package_data={'pk_core' : []},
    include_package_data=True,
    install_requires=[
    ],
    scripts=[],
    entry_points={
        'console_scripts' : [],
    },
    data_files=[
    ],
    test_suite='nose2.collector.collector',
    tests_require=['nose2'],
    zip_safe=False
)


