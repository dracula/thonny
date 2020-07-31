from setuptools import setup
import os

#setupdir = os.path.dirname(__file__)

setup(
    name='thonny-dracula',
    version='0.1.1',
    description='Dracula dark theme for Thonny IDE',
    long_description=open('README.md').read(),
    url='https://github.com/danspinola/thonny',
    download_url='https://github.com/danspinola/thonny',
    author='Daniel Spinola',
    author_email='dspinola.dev@gmail.com',
    license='MIT',
    packages=["thonnycontrib.dracula"],
    include_package_data = True,
    install_requires=["thonny >= 3.0.0"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Embedded Systems",

        ],
    keywords="IDE education programming Thonny dark theme dracula",
    platforms=["Windows", "macOS", "Linux"],
    )