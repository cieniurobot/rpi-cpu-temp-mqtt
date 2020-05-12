import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpi-cpu-temp-mqtt",
    version="0.0.1",
    author="cieniurobot",
    author_email="marcin@cieniu.pl",
    description="MQTT publisher for Raspberry Pi CPU temperature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cieniurobot/rpi-cpu-temp-mqtt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.6',
)
