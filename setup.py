from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='heat_index',
    version='0.0.1',
    description='A simple tool to calculate heat index in Python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Myles Fang',
    author_email='i@myles.hk',
    keywords=['HeatIndex'],
    url='https://github.com/myleshk/heat_index_calculator',
    download_url='https://pypi.org/project/heat_index_calculator/'
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
