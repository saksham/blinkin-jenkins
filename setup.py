from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='blinkin-jenkins',
      version=version,
      description="Connecting traffic light to CI Jenkins using Raspberry Pi",
      long_description="""""",
      classifiers=[],# Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='traffic-light jenkins raspberry-pi sketching electronics',
      author='Saksham Gautam',
      author_email='saksham@no-reply.github.com',
      url='http://github.com/saksham/blinkin-jenkins',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          "python-jenkins",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
