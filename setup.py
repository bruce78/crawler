from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()
setup(
    name='Crawler',
    version='0.0.1',
    description='Crawler project',
    long_description=readme,
    install_requires=['python-dateutil>=2.7.3', 'requests==2.19.1',
                      'APScheduler==3.0.0', 'lxml==4.2.3', 'cssselect==1.0.3'],

    author='Kevin Zhao',
    author_email='rhtbapat@gmail.com',
    url='https://github.com/rhtbapat/BasicStructure',
    license=license,
    packages=find_packages()
)
