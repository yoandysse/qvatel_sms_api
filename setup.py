from setuptools import setup

setup(
    name='qvatel_sms_api',
    version='1.0',
    packages=['qvatel'],
    url='',
    license='',
    author='Yoandy Isse',
    author_email='yoandysse@gmail.com',
    description='Una librería de Python para enviar SMS a través de QvaTel.com',
    install_requires=[
        'requests>=2.31.0,<3.0.0'
    ]
)

