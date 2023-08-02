from setuptools import find_packages, setup

def get_requirements(filepath):
    '''
    Returns the list of required packages from the requirements file
    '''
    with open(filepath) as file:
        libs = file.readlines()
        requirements = [lib.replace("\n", "") for lib in libs]
        if "-e ." in requirements:
            requirements.remove("-e .")

        return requirements


setup(
    name = 'ML_project',
    version = '0.0.1',
    author = 'Nikhil',
    author_email = 'relativity1999@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)