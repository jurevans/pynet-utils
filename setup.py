from setuptools import setup, find_packages

setup(
    name="pynet",
    version="0.1.0",
    packages=find_packages(exclude=[]),
    install_requires=[
        "click",
    ],
    entry_points={
        'console_scripts': [
            'pynet=pynet.main:cli'
        ]
    }
)
