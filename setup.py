from setuptools import setup, find_packages

setup(
    name='ML_Pairs_Trading',
    version='0.1.0',  # Initial version
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'statsmodels',
        'scikit-learn',
        'tensorflow',
        'matplotlib',
        'seaborn',
        'yfinance',
        'ta-lib',
        'backtrader',
    ],
)
