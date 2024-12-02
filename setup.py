from setuptools import setup, find_packages

setup(
    name='mcm-python',  # Name of your package
    version='0.1',  # Version number
    packages=find_packages(),  # Find all packages in the current directory
    install_requires=[],  # List of dependencies (empty for now)
    author='Ariyan',
    author_email='ariyan@mycountrymobile.com',
    description='A simple Python package',
    long_description=open('README.md').read(),  # Read the content of README.md
    long_description_content_type='text/markdown',
    url='https://github.com/Mycountrymobile-com/mcm-python/',  # Replace with your actual GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',  # Compatible with Python 3
        'License :: OSI Approved :: MIT License',  # License used for the package
        'Operating System :: OS Independent',  # Works on any OS
    ],
)
