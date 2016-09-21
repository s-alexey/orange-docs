from setuptools import setup

__version__ = __import__('orangedocs').__version__

setup(
    name='sphinx-orange-extension',
    version=__version__,
    author='',
    author_email='',
    url='http://github.com/s-alexey/orange-docs',
    license='GPLv3+',
    description='Sphinx orange extension. Prevent documentation from duplication and inconsistency.',
    packages=['orangedocs'],
)
