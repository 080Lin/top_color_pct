from setuptools import find_packages, setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

setup(
    name='top_colors_pct',
    packages=find_packages(),
    version='0.1.2',
    description='This library allows you to take N top colors from the image',
    author='NasciNSC',
    long_description_content_type='text/markdown',
    long_description=long_description,
    license='MIT',
    install_requires=['webcolors'],
    keywords=['python', 'image', 'processing', 'img', 'top_colors', 'color', 'analitics'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ]
)