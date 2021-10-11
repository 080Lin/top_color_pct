from setuptools import find_packages, setup

setup(
    name='top_colors_pct',
    packages=find_packages(),
    version='0.1.0',
    description='This library allows you to take N top colors from the image',
    author='NasciNSC',
    license='MIT',
    install_requires=['webcolors'],
    keywords=['python', 'image', 'processing', 'img', 'top_colors', 'color'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ]
)