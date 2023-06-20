from setuptools import setup


repo_name = "recommendation_system_project"
author_name = "Ronald"
src_repo = "src"
list_of_requirements = ['streamlit', 'numpy']

setup(
    name = src_repo,
    version='0.0.1',
    author = author_name,
    description='book recommender',
    url="https://github.com/Ronaldonyagaka/recommendation_system_project",
    author_email='nyagaka@outlook.com',
    packages=[src_repo],
    python_requires = ">=3.7",
    install_requires = list_of_requirements
    )