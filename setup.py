#This script is used to define my python project as a package

from setuptools import find_packages, setup

setup (
    name = "Generative AI Project",
    version = "0.0.0",
    author = "Mbali Sithebe",
    author_email = "mbaleeyenkosi@gmail.com",
    packages = find_packages (),
    install_requires = []
)