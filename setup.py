from setuptools import setup

setup(
    name='heater',
    packages=['heater'],
    include_package_data=True,
    install_requires=[
        'flask',
        'RPi.GPIO',
    ],
)
