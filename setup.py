from setuptools import setup, find_packages

setup(
    name="endor-dependabot-python-repro",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.8,<3.9",
    install_requires=[
        "Flask==2.1.2",
        "PyYAML==5.1",
        "cryptography==37.0.2",
        "requests==2.32.3",
    ],
    description="Minimal repo to reproduce Endor dependabot Python 3.8 issues",
)