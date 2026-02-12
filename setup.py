from setuptools import setup, find_packages

setup(
    name="rockyscan",
    version="2.0.0",
    author="Rocky Patel",
    description="Unified CLI Network Scanning Framework",
    packages=find_packages(),
    install_requires=[
        "rich",
        "pyfiglet"
    ],
    entry_points={
        "console_scripts": [
            "rockyscan=rockyscan.main:main"
        ]
    },
    python_requires=">=3.8",
)
