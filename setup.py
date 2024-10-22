'''The setup.py file plays a crucial role in Python projects, especially for packaging and distribution. Here are its main functions:

Package Definition: It defines the package name, version, author, and other metadata.
Dependencies: It specifies any external libraries or dependencies required for the project, allowing for easy installation via pip.
Entry Points: It can define entry points for command-line scripts, making it easier to run the application or use it as a module.
Build and Distribution: It facilitates the building of source distributions and binary distributions, making it easier to share and distribute your package.
Installation: Running python setup.py install installs the package and its dependencies into the Python environment.

Including -e . in your requirements.txt installs the package in editable mode, allowing immediate reflection of any code changes in your environment. It runs setup.py to gather metadata and creates a symbolic link to the package directory. This is beneficial for efficient development and real-time testing of changes.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirement() -> List[str]:
    '''
    This function will return the list of requirement
    '''

    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as requirement_file:

            read_pkg_lines = requirement_file.readlines()

            for requirement_line in read_pkg_lines:
                requirement = requirement_line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found.")

    return requirement_lst

setup(
    name="LoanApproval",
    version="0.0.1",
    author="Muhammad Ali",
    author_email="muhammadalimsc21@gmail.com",
    description='Loan Approval - END TO END Machine Learning Project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/muhammadali-msc/LoanApprovalPrediction',
    packages=find_packages(),
    install_require=get_requirement()
)
