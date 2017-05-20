try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="NoseWhistleblower",
    author="Francis Lavoie",
    author_email="lav.francis@gmail.com",
    url="https://github.com/francisl/nosewhistleblower",
    version="0.2.0",
    packages=[
        "nosewhistleblower"
    ],
    tests_require=["mock>1.0.0"],
    install_requires=[
        "nose",
        "setuptools"
    ],
    test_suite='tests',
    license="MIT License",
    description="Notify the completion and status for all your tests running in the background",
    long_description=open("README.md").read(),
    entry_points={
        'nose.plugins.0.10': [
            'NoseWhistleblower = nosewhistleblower.plugin:NoseWhistleblower'
        ]
    },
    include_package_data=True,
)
