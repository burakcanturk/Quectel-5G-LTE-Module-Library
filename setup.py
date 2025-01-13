from setuptools import setup

setup(
    name="quectel_at",  # Projenizin adı (benzersiz olmalı)
    version="1.0.0",  # Versiyon numarası
    author="Burak Cantürk",
    author_email="burakcanturk12@gmail.com",
    description="This is a library for Quectel Modules.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/burakcanturk/Quectel-5G-LTE-Module-Library.git",
    packages=["QuectelAT"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyserial"],  # Eğer dış bağımlılıklar varsa buraya ekleyin
)
