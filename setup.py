from setuptools import setup

setup(
    name="lciafmt",
    version="0.4.1",
    packages=["lciafmt"],
    package_dir={'lciafmt': 'lciafmt'},
    package_data={'lciafmt': ["data/*.*"]},
    include_package_data=True,
    install_requires=["fedelemflowlist @ git+git://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List@v1.0.7#egg=fedelemflowlist",
                      "esupy @ git+https://github.com/USEPA/esupy",
                      "olca-ipc", "pandas", "xlrd",
                      "pyyaml>=5.3",
                      "pyodbc>=4.0.30",
                      ],
    license="CC0",
    author='Michael Srocka, Troy Hottle, Ben Young, Wesley Ingwersen, Ben Morelli',
    author_email='ingwersen.wesley@epa.gov',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: IDE",
        "Intended Audience :: Science/Research",
        "License :: CC0",
        "Programming Language :: Python :: 3.x",
        "Topic :: Utilities",
    ],
)
