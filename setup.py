from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.4"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME= "databaseautomation"
AUTHOR_USER_NAME = "sunnysavita10"
AUTHOR_EMAIL = "sunny.savita@ineuron.ai"

setup(
    name= "MongoDB_VectorDB",
    version="0.0.4",
    author="Jasper Bongers",
    author_email="jasper.bongers@yahoo.com",
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )