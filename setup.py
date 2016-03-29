from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='pytemplate',
    version='0.4',
    packages=find_packages(),
    scripts = ['pytemplate.py', 'secretary.py'],
    install_requires = ['jinja2'],
#    entry_points={
#	    'pytemplate': [
#		    'pytemplate = pytemplate',
#		    ]
#	    },
    author = "Yuri V. Yakovlev",
    author_email = "krotos139@gmail.com",
    description = "Template processor",
    license = "GPL v3",
    keywords = "jinja2 odt text template",
    url = "https://github.com/krotos139/pytemplate",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
