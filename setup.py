from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='pytemplateproc',
    version='0.4.2',
    packages=find_packages(),
    scripts = [
	    'pytemplate.py', 
	    'secretary.py',
	    'tests.py'],
    install_requires = ['jinja2'],
    test_suite='tests',
    include_package_data=True,
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
