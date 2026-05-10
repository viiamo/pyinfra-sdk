from setuptools import setup, find_packages
setup(
    name="pyinfra-sdk",
    version="2.8.1",
    description="Python infrastructure automation SDK",
    long_description="SDK for managing servers, containers, and deployments.",
    author="pyinfra Team",
    author_email="team@pyinfra.dev",
    url="https://github.com/pyinfra-dev/pyinfra-sdk",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["requests>=2.25.0"],
)