from setuptools import find_packages
from setuptools import setup

from apps_sal import __version__

with open('./README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='apps-sal',
    version=__version__,
    description='APPS dataset refined by SAL',
    long_description=LONG_DESCRIPTION,
    url='https://prl.korea.ac.kr',
    download_url='https://github.com/kupl/apps-sal',
    author='Software Analysis Laboratory, Korea University',
    python_version='>=3.7',
    packages=find_packages(include=('apps_sal',)),
    include_package_data=True,
    setup_requires=[],
    install_requires=[
        'tabulate'
    ],
    dependency_links=[],
    entry_points={
        'console_scripts': [
            'apps-sal=apps_sal.bin:main'
        ]
    }
)
