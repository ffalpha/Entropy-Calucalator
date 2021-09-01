from setuptools import setup,find_packages


setup(
    name='Shanon entropy',
    version='0.0.0',
    description='entropy is a command line friend that helps you reduce entropy in your life',
    long_description=open('README.md',encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    author='Kalana Mihiranga',
    author_email='kalanam217@gmail.com',
    license='MIT',
    keywords=['entropy', 'shannon', 'journaling'],
    url='https://github.com/h4ck3rk3y/entropy',
    packages=find_packages()
  )