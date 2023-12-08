from setuptools import setup, find_packages

setup(
    name='dynamics_learner',
    author='Samuel Mindel',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'manim',
        'sympy',
    ],
)