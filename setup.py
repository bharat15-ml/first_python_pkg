from setuptools import setup, find_packages

setup(
    name="my_first_pkg",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Bharat B Singh",
    description="A simple math operations package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bharat15-ml/first_python_pkg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

