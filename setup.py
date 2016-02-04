from setuptools import setup
import os
import sys
if sys.version_info[0] < 3:
    from codecs import open

with open(os.path.join(os.path.dirname(__file__), 'README.rst'),
          'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='nlcontinuous',
    py_modules=['nlcontinuous'],
    package_data={
        '': [
            'README.rst',
            'LICENSE',
        ]
    },
    version='0.0.3',
    author='TylerTemp',
    author_email='tylertempdev@gmail.com',
    url='https://github.com/TylerTemp/md-nlcontinuous',
    download_url='http://github.com/TylerTemp/md-nlcontinuous/zipball/master/',
    license='GPLv3',
    description=('Prevent white space for Chinese break line '
                 'in markdown paragraph'),
    keywords='markdown',
    long_description=long_description,
    install_requires=[
        'markdown',
    ],
    platforms='any',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        ],
)
