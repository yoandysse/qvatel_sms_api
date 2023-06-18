from setuptools import setup

setup(
    name='qvatel_sms_api',
    version='1.0.5',
    packages=['qvatel'],
    url='https://github.com/yoandysse/qvatel_sms_api.git',
    license='MIT',
    author='Yoandy Isse',
    author_email='yoandysse@gmail.com',
    description='Una librería de Python para enviar SMS a través de QvaTel.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['sms', 'qvatel', 'api', 'python', 'enviar sms', 'sms masivos', 'sms marketing', 'sms api', 'sms gateway'],
    install_requires=[
        'requests>=2.31.0,<3.0.0'
    ]
)
