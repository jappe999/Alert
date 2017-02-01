#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='Alert',
      version='1.0.0',
      description='Alert the user.',
      long_description='Alert the user if he/she is using the computer too long.',
      author='Jappe999',
      author_email='jappe999@github.com',
      url='http://github.com/jappe999/Alert',
      keywords='Alert time Linux',
      install_requires=[
        'pyautogui'
      ]
)
