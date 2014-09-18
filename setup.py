from setuptools import setup, find_packages


setup(name='hipfab',
      description='Hipchat integration for Fabric',
      author='Inkling',
      url='https://www.inkling.com/',
      version='0.1.0',
      license='Apache License, Version 2.0',
      provides=['hipfab'],
      install_requires=['requests', 'fabric'],
      packages=find_packages(exclude=['examples']),
)
