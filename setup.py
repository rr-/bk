from setuptools import setup

setup(
    name             = 'bk',
    packages         = ['bk'],
    version          = '0.2',
    description      = 'An utility that lets you change desktop background for GNU/Linux and Windows.',
    author           = 'rr-',
    author_email     = 'rr-@sakuya.pl',
    url              = 'https://github.com/rr-/bk',
    download_url     = 'https://github.com/rr-/bk/tarball/0.2',
    keywords         = ['wallpaper', 'screen', 'monitor', 'desktop'],
    install_requires = ['screeninfo', 'pillow'],
    scripts          = ['bk/bk'],
    classifiers      = [],
)
