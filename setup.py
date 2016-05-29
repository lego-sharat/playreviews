from setuptools import setup

setup(
    name = 'playreviews',
    packages = ['playreviews'],
    version = '0.1',
    description = 'Package to scrape google play store reviews',
    author = 'Sharat Chandra',
    author_email = 'sharat9211@gmail.com',
    url = 'https://github.com/sharat9211/playreviews',
    keywords = ['google play store reviews', 'reviews', 'play store'],
    classifiers = [],
    install_requires = [
        'requests',
        'beautifulsoup4',
    ]

)