from setuptools import setup, find_packages
import sys, os

version = '0.0'
long_description = open('README.txt').read()

setup(name='opencore_unconfirmedmembers',
      version=version,
      description="a web view for opencore to facilitate management of pending sitewide memberships",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Ethan Jucovy',
      author_email='ejucovy@gmail.com',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[

      ],
      entry_points="""
      [opencore.versions]
      opencore_unconfirmedmembers = opencore_unconfirmedmembers
      [topp.zcmlloader]
      opencore = opencore_unconfirmedmembers
      """,
      )
