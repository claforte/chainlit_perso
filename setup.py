"""Python setup.py for chainlit_perso package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("chainlit_perso", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="chainlit_perso",
    version=read("chainlit_perso", "VERSION"),
    description="Awesome chainlit_perso created by claforte",
    url="https://github.com/claforte/chainlit_perso/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="claforte",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["chainlit_perso = chainlit_perso.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
