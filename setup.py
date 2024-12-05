from pathlib import Path

from setuptools import setup

# "import" __version__
__version__ = '0.9.5'

setup(
    name='nbsphinx',
    version=__version__,
    package_dir={'': 'src'},
    packages=['nbsphinx'],
    package_data={'nbsphinx': [
        '_static/nbsphinx-code-cells.css_t',
        '_static/nbsphinx-gallery.css',
        '_static/nbsphinx-no-thumbnail.svg',
        '_static/nbsphinx-broken-thumbnail.svg',
        '_texinputs/nbsphinx.sty',
    ]},
    python_requires='>=3.6',
    install_requires=[
        'docutils>=0.18.1',
        'jinja2',
        'nbconvert>=5.3,!=5.4',
        'traitlets>=5',
        'nbformat',
        'sphinx>=1.8',
    ],
    author='Matthias Geier',
    author_email='Matthias.Geier@gmail.com',
    description='Jupyter Notebook Tools for Sphinx',
    long_description=Path('README.rst').read_text(),
    license='MIT',
    keywords='Sphinx Jupyter notebook'.split(),
    url='https://nbsphinx.readthedocs.io/',
    project_urls={
        'Documentation': 'https://nbsphinx.readthedocs.io/',
        'Source Code': 'https://github.com/spatialaudio/nbsphinx/',
        'Bug Tracker': 'https://github.com/spatialaudio/nbsphinx/issues/',
    },
    platforms='any',
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Framework :: Jupyter',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
    ],
)
