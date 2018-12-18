import setuptools
import sys

script_paths = [
    'bin/pystack'
]
is_windows = hasattr(sys, 'getwindowsversion')
if is_windows:
    script_paths = [
        'bin\pystack.bat'
    ]

with open('README.md', 'r') as fh:
    long_description = fh.read()

print(script_paths)

setuptools.setup(
    name='pystack_cli',
    version='1.0.0',
    author='Zoltan Csontos',
    author_email='zoltan.csontos.dev@gmail.com',
    description='PyStack micro-framework command line interface',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zoltancsontos/pystack.sh-cli',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    scripts=script_paths
)
