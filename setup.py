#!/usr/bin/env python
#
# PySceneDetect setup.py
#


import glob
import sys

from setuptools import setup
import py2exe

if sys.version_info < (2, 6) or (3, 0) <= sys.version_info < (3, 3):
    print('PySceneDetect requires at least Python 2.6 or 3.3 to run.')
    sys.exit(1)


def get_requires():
    requires = ['numpy']
    if sys.version_info == (2, 6):
        requires += ['argparse']
    return requires


setup(
    name='PySceneDetect',
    version='0.3.6',
    description="A cross-platform, OpenCV-based video scene detection program and Python library. ",
    long_description=open('package-info.rst').read(),
    author='Brandon Castellano',
    author_email='brandon248@gmail.com',
    url='https://github.com/Breakthrough/PySceneDetect',
    license="BSD 2-Clause",
    keywords="video computer-vision analysis",
    install_requires=get_requires(),
    extras_require={
        #'GUI': ['gi'],
        #'VIDEOENC': ['moviepy']
    },
    packages=['scenedetect'],
    package_data={'': ['../LICENSE*', '../USAGE.md', '../package-info.rst']},
    #include_package_data = True,   # Only works with this line commented.
    #test_suite="unitest.py",
    entry_points={"console_scripts": ["scenedetect=scenedetect:main"]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Multimedia :: Video :: Non-Linear Editor',
        'Topic :: Utilities'
    ],
    options = {
        'py2exe' : {
            'compressed': True,
            'bundle_files': 1,
            'dist_dir': 'dist',
            "dll_excludes": ['api-ms-win-mm-time-l1-1-0.dll', 'api-ms-win-core-registry-l2-2-0.dll', 'api-ms-win-core-privateprofile-l1-1-1.dll', 'api-ms-win-core-stringansi-l1-1-0.dll', 'api-ms-win-core-heap-obsolete-l1-1-0.dll', 'api-ms-win-core-largeinteger-l1-1-0.dll', 'api-ms-win-core-libraryloader-l1-2-2.dll', 'api-ms-win-core-string-obsolete-l1-1-0.dll', "MSVCP90.dll","libzmq.pyd","geos_c.dll","api-ms-win-core-string-l1-1-0.dll","api-ms-win-core-registry-l1-1-0.dll","api-ms-win-core-errorhandling-l1-1-1.dll","api-ms-win-core-string-l2-1-0.dll","api-ms-win-core-profile-l1-1-0.dll","api-ms-win*.dll","api-ms-win-core-processthreads-l1-1-2.dll","api-ms-win-core-libraryloader-l1-2-1.dll","api-ms-win-core-file-l1-2-1.dll","api-ms-win-security-base-l1-2-0.dll","api-ms-win-eventing-provider-l1-1-0.dll","api-ms-win-core-heap-l2-1-0.dll","api-ms-win-core-libraryloader-l1-2-0.dll","api-ms-win-core-localization-l1-2-1.dll","api-ms-win-core-sysinfo-l1-2-1.dll","api-ms-win-core-synch-l1-2-0.dll","api-ms-win-core-heap-l1-2-0.dll","api-ms-win-core-handle-l1-1-0.dll","api-ms-win-core-io-l1-1-1.dll","api-ms-win-core-com-l1-1-1.dll","api-ms-win-core-memory-l1-1-2.dll","api-ms-win-core-version-l1-1-1.dll","api-ms-win-core-version-l1-1-0.dll"]
        }
    },
    console=['scenedetect.py']
)
