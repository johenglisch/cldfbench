from setuptools import setup, find_packages


setup(
    name='cldfbench',
    version='0.3.0',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    description='Python library implementing a CLDF workbench',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='',
    license='Apache 2.0',
    url='https://github.com/cldf/cldfbench',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'cldfbench=cldfbench.__main__:main',
        ],
    },
    platforms='any',
    python_requires='>=3.5',
    install_requires=[
        'csvw>=1.5.6',
        'cldfcatalog>=1.1',
        'clldutils>=3.1.2',
        'pycldf>=1.8.1',
        'xlrd',
        'openpyxl',
        'termcolor',
        'requests',
    ],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'mock',
            'pytest>=3.6',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
            'pyglottolog',
            'pyconcepticon',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
