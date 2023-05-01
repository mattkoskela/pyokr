import os
from setuptools import setup

LONG_DESC = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

with open("okr/version.py") as f:
    exec(f.read())

setup(
    name="okr",
    version=__version__,
    author="Matt Koskela",
    author_email="mattkoskela@gmail.com",
    packages=["okr"],
    url="https://github.com/mattkoskela/pyokr",
    include_package_data=True,
    zip_safe=False,
    license="LICENSE.txt",
    description="Python based web interface for an OKR manager",
    long_description=LONG_DESC,
    install_requires=[
        "flask==2.3.2",
        "flask-login==0.2.10",
        "sqlalchemy==0.9.4",
        "flask-sqlalchemy==1.0"
    ]
)
