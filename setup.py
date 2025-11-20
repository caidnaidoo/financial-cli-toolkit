from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="finance-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A command-line financial data toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "pandas>=1.5.0", 
        "rich>=12.0.0",
        "click>=8.1.0",
        "yfinance>=0.2.18",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'fquote=src.main:quote',
            'fhist=src.main:hist',
            'finance-cli=src.main:cli',
        ],
    },
)