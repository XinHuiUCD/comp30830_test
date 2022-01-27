from setuptools import setup

setup(
    name='Setup File for Q2 in Lab2',
    version='1.0',
    scripts=['q2.py'],
    entry_points={
        'console_scripts': ['my-command=q2:main']
    },
)