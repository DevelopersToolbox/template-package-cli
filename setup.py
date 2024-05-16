# setup.py

"""Setup script."""

from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='baseline-package',
    version='0.0.1rc2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'baseline-package=baseline_package.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='A nice description will go here',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/GreyTeamToolbox/baseline-package',
    project_urls={
        ' Source': 'https://github.com/GreyTeamToolbox/baseline-package',
        ' Tracker': 'https://github.com/GreyTeamToolbox/baseline-package/issues/',
        ' Documentation': 'https://github.com/GreyTeamToolbox/baseline-package',
        ' Funding': 'https://ko-fi.com/wolfsoftware',
        ' Say Thanks!': 'https://github.com/sponsors/TGWolf',
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
