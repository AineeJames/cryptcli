from setuptools import find_packages, setup

setup(
    name='cryptcli',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'typer',
        'rich',
        'plotext',
        'inquirer',
    ],
    entry_points='''
    [console_scripts]
    crypt=cryptcli:app
    ''',
)

print("setup")
