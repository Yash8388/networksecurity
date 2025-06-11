'''
The setup.py file is an essential part of packaging and
distrubuting python projects. It is used by setup tools
(or distutils in older Python versions) to define the configuration
of your project, sucj as its metadata, dependencies, and more.

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements.
    """
    requirement_list:List[str] =[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)


    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Yash Patil",
    author_email="patilyash5999@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements()
)