from setuptools import setup, find_packages

setup(
    name="zksync2",
    version="0.6.0",  # Use_scm_version overrides this if enabled
    author="Danijel Radakovic",
    author_email="danijel@txfusion.io",
    description="zkSync2 python client sdk",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zksync-sdk/zksync2-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    use_scm_version={
        "write_to": "zksync2/_version.py",
        "fallback_version": "0.6.0",
    },
    setup_requires=['setuptools_scm'],
    # Add other arguments as necessary
)
