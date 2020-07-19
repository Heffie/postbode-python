from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="postbode-python-JeffreyHagenstein",  # Replace with your own username
    version="0.0.1",
    author="Jeffrey Hagenstein",
    author_email="jdhagenstein@gmail.com",
    description="Python wrapper for api of http://www.postbode.nu for sending postal mail.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Heffie/postbode-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
