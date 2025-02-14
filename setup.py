from setuptools import setup, find_packages

setup(
    name="rarity-module",  # Package name
    version="0.1.0",  # Initial version
    author="Your Name",
    author_email="your@email.com",
    description="A module for calculating rarity scores",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jelo819/rarity-module",  # Replace with your repo URL
    packages=find_packages(),  # Automatically discover all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version
    install_requires=[],  # Add dependencies if needed
)
