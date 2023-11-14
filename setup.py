from setuptools import setup, find_packages

setup(
    name='httprober',
    version='1.0.1',
    author='D. Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description='A fast alive subdomains finder with new generation HTTPX client',
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.4',
        'httpx==0.25.1',
        'requests==2.31.0',
        'argparse==1.4.0',
        'setuptools==68.1.2'
    ],
    entry_points={
        'console_scripts': [
            'httprober = httprober.httprober:main'
        ]
    },
)
