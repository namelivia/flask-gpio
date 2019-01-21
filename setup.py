from setuptools import setup

setup(
    name='flask-gpio',
    packages=['flask-gpio'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flup',
        'RPi.GPIO',
    ],
)
