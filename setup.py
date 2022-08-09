from setuptools import setup, find_packages

setup(
    name="pynet",
    version="1.0",
    summary="Python-based CLI network tools",
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
