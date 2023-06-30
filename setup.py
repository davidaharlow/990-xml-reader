from distutils.core import setup
import os

NAME = 'zenitechcyber_irsx'
HUMAN_NAME = 'zenitechcyber_irsx'
HERE = os.path.abspath(os.path.dirname(__file__))
version_ns = {}
with open(os.path.join(HERE, 'irs_reader', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup(name=HUMAN_NAME,
      description = "Turn the IRS' versioned XML 990's into python objects \
        with original line number and description.",
      version = version_ns['__version__'],
      author = 'David Harlow',
      author_email = 'david@uptokyn.com',
      url = 'https://github.com/davidaharlow/990-xml-reader',
      license = 'MIT',
      setup_requires = ["setuptools", ],
      install_requires = ['requests', 'xmltodict', 'unicodecsv'],
      tests_require = ['nose', 'requests', 'xmltodict', 'unicodecsv', 'tox', 'tox-pyenv',],
      packages = ['irsx'],
      package_dir = {'irsx': 'irs_reader'},
      package_data = {'irsx': ['metadata/*.csv']},
      keywords = ['990', 'nonprofit', 'tax'],
      entry_points = {
          "console_scripts": ["zenitechcyber_irsx=irsx.irsx_cli:main",
                              "zenitechcyber_irsx_index=irsx.irsx_index_cli:main",
                              "zenitechcyber_irsx_retrieve=irsx.irsx_retrieve_cli:main"]
      },
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',

        ],
      )
