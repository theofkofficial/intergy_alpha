from setuptools import setup, find_packages
import modules

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Intergy Alpha",
    version=modules.__version__,
    author='Ömer Faruk Kılıç',
    author_email='omerfaruk.kilic1@bahcesehir.edu.tr',
    description="Finergy Baseline Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'python-dateutil',
        'openpyxl',
        'PySimpleGUI',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

