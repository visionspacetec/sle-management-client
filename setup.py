from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sle-management-client",
    version="0.0.1",
    author="VisionSpace Technologies GmbH",
    author_email="oss@visionspace.com",
    description="Python Space Link Extension Management Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="www.visionspace.com",
    license="AGPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3"
    ],
    python_requires=">=3",
    keywords="sle management client",
    install_requires=["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"],
    packages=find_packages(exclude=['build', '*.build', 'build.*', '*.build.*',
                                    'dist', '*.dist', 'dist.*', '*.dist.*',
                                    'examples', '*.examples', 'examples.*', '*.examples.*',
                                    'tests', '*.tests', 'tests.*', '*.tests.*']),
    include_package_data=True,
)
