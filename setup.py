from setuptools import setup

version = '0.3'

setup(
    name='bitly_api',
    version=version,
    description="An API for bit.ly",
    long_description=open("./README.md", "r").read(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords='bitly bit.ly',
    author='Jehiah Czebotar - updated - Paolo Galeone',
    author_email='jehiah@gmail.com - updated - nessuno@nerdz.eu',
    url='https://github.com/galeone/bitly-api-python',
    license='Apache Software License',
    packages=['bitly_api'],
    include_package_data=True,
    zip_safe=True,
)
