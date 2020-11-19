from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

# See Pipfile for checking dependencies
setup(
    name="pylogger",
    version="0.0.1",
    description="Python logger for every project using Python.",
    long_description=readme,
    url="https://github.com/estie-inc/python-logger",
    packages=find_packages(exclude=("tests", "docs")),
)
