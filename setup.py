try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pystocktw',
    version='0.0.1',
    url='https://github.com/carryme9527/pystocktw/',
    license='BSD',
    author='carryme9527',
    author_email='carryme9527@gmail.com',
    description='pystocktw',
    packages=['pystocktw'],
)
