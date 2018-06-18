#!/usr/bin/env python

"""Kegbot API client library.

For more information and documentation, see http://kegbot.org/docs
"""

VERSION = '1.2.0'
DOCLINES = __doc__.split('\n')
SHORT_DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])

def setup_package():
  from setuptools import setup, find_packages

  setup(
      name = 'kegbot-api',
      version = VERSION,
      description = SHORT_DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      author = 'Bevbot LLC',
      author_email = 'info@bevbot.com',
      url = 'http://kegbot.org/',
      packages = find_packages(exclude=['testdata']),
      namespace_packages = ['kegbot'],
      install_requires = [
        'kegbot-pyutils',
        'python-gflags',
        'protobuf',
        'requests',
      ],
      dependency_links = [
          'https://github.com/jakogut/kegbot-pyutils/tarball/master#egg=v0.2'
      ],
      include_package_data = True,
  )

if __name__ == '__main__':
  setup_package()
