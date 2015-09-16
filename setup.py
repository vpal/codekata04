from setuptools import setup

setup(
    name='codekata04',
    version='0.1',
    packages=['codekata04'],
    url='',
    license='',
    author='vpal',
    author_email='',
    description='',
    entry_points={
        'console_scripts': [
            'kata04_part_one=codekata04.kata04_part_one:main',
            'kata04_part_two=codekata04.kata04_part_two:main',
            'kata04_part_three=codekata04.kata04_part_three:main'
        ],
    },
    test_suite='tests'
)