from setuptools import setup

def parse_requirements(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

setup(
    name="quectel_at",  # Projenizin adı (benzersiz olmalı)
    version="1.1.0",  # Versiyon numarası
    author="Burak Cantürk",
    author_email="burakcanturk12@gmail.com",
    description="This is a library for Quectel Modules.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/burakcanturk/Quectel-5G-LTE-Module-Library.git",
    packages=["QuectelAT"],
    install_requires=parse_requirements("requirements.txt"),  # Eğer dış bağımlılıklar varsa buraya ekleyin
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
