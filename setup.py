from setuptools import find_packages, setup


setup(
    name='kuntal_test_lib',
    packages=find_packages(include=['kuntal_test_lib']),
    version='0.1.0',
    description='Kuntal first Python library',
    author='Kuntal',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
