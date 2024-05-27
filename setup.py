# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.template-package-cli',
    version='0.1.0',
    packages=['wolfsoftware.template_package_cli'],
    entry_points={
        'console_scripts': [
            'template-package-cli=wolfsoftware.template_package_cli.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='A nice description will go here',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DevelopersToolbox/template-package-cli',
    project_urls={
        ' Source': 'https://github.com/DevelopersToolbox/template-package-cli',
        ' Tracker': 'https://github.com/DevelopersToolbox/template-package-cli/issues/',
        ' Documentation': 'https://github.com/DevelopersToolbox/template-package-cli',
        ' Sponsor': 'https://github.com/sponsors/WolfSoftware',
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
