from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .' 
'''
 This triggers the setup.py but not needed in the requirement list
'''

def get_requirements(file_path:str)-> List[str]:
    '''
    This function returns the list of requirements !!
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n"," ")for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements            




#Meta data information about the project
setup(
name = 'mlproject',
version = '0.0.1',
author = 'Baisakhi Mal',
author_email = 'baisakhi.mal@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)