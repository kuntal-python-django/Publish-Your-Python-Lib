from setuptools import find_packages, setup
import pathlib


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name='kuntal_test_lib',                                 # required
    
    packages=find_packages(include=['kuntal_test_lib']),    # required
    # packages=find_packages(exclude=("tests",)),
    
    version='1.5.0',                                        # required
    # license='MIT',
    description='Kuntal first Python library',
    long_description=README,
    long_description_content_type="text/markdown",

    author='Kuntal',
    author_email="kuntal.samanta@gmail.com",

    url="https://github.com/kuntal-python-django/Publish-Your-Python-Lib",
    # download_url="https://github.com/kuntal-python-django/Publish-Your-Python-Lib/archive/v_0_0_1.tar.gz",
    
    setup_requires=['wheel'],
    # install_requires=['A>=1,<2', 'B>=2']
    # install_requires=['numpy', 'requests'],
    
    # keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
    # classifiers=["Programming Language :: Python :: 3", "Programming Language :: Python :: 3.7"],
    # include_package_data=True,
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest==4.4.1'],
    # test_suite='tests',
    entry_points={
        "console_scripts": [
            "entry_call = kuntal_test_lib.__main__:main",
        ]
    },
)
