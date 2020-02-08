from setuptools import setup, find_packages

__author__ = "Dax Mickelson"
__author_email = "dmickels@cisco.com"
__license__ = "BSD"

setup(
    name="dnacsdk",
    version="20200208.0",
    description="Easier interface to Cisco's DNA Center API than writing your own way.",
    long_description="""Automation of our networks is the current trend.  However, network engineers aren't proficient
    programmers.  Thus, a "helper library" is needed to more quickly bootstrap them into being able to write scripts
    that work.""",
    url="https://github.com/daxm/dnacsdk",
    author="Dax Mickelson",
    author_email="dmickels@cisco.com",
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    keywords="dnacsdk DNA DNAC Cisco networking API",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=["requests", "datetime", "ipaddress"],
    python_requires=">=3",
    package_data={},
    data_files=None,
)
