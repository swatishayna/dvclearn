from setuptools import setup

with open("Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="swati",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swatishayna/dvclearn",
    author_email="swati308mmu@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
