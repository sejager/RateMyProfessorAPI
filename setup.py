import pathlib
import setuptools

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='RateMyProfessorAPI',
    version='1.4.0',
    description='Python web scraper to get professor ratings from ratemyprofessor.com website.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sejager/RateMyProfessorAPI',
    author='Sebastian Gyger',
    author_email='sebigyger@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.12',
    include_package_data=True,
    install_requires=requirements,
    project_urls={
        'Issue Tracker': 'https://github.com/sejager/RateMyProfessorAPI/issues',
    }
)
