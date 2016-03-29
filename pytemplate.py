#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
#from lxml import objectify
import jinja2
from jinja2 import Environment, PackageLoader, FileSystemLoader, BaseLoader, nodes
from jinja2.ext import Extension
import csv
import sqlite3
import sys
import logging
from optparse import OptionParser
import hashlib
import os
import secretary

def UnicodeDictReader(utf8_data, **kwargs):
	csv_reader = csv.DictReader(utf8_data, **kwargs)
	for row in csv_reader:
		yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])


@jinja2.contextfunction
def load_csv(context, arg):
	logging.info("Read CSV (%s)" % arg)
	csvfile = open(arg, 'rt')
	csvreader = UnicodeDictReader(csvfile)
	csvdata = list(csvreader)
	csvfile.close()
	logging.info("Read %d lines" % len(csvdata))
	return csvdata

@jinja2.contextfunction
def load_xml(context, arg):
	logging.info("Read XML (%s)" % arg)
	#e = objectify.parse(arg)
	e = ET.parse(arg).getroot()

	logging.info("e = %s" % str(e))
	return e

@jinja2.contextfunction
def load_sqlite(context, arg):
	logging.info("Read SQLite (%s)" % arg)
	conn = sqlite3.connect(arg)
	c = conn.cursor()
	return c

@jinja2.contextfunction
def load_text(context, arg):
	logging.info("Read TEXT file (%s)" % arg)
	f = open(arg, 'r')
	result = f.read()
	f.close()
	return result.decode('utf-8')

@jinja2.contextfunction
def le(context, arg):
	if arg == None:
		return ""
	return arg.replace("_", "\_").replace("&","\&")

@jinja2.contextfunction
def log(context, arg):
	logging.debug(arg)
	return ""

@jinja2.contextfunction
def file_md5(context, arg):
	logging.info("File (%s) -> MD5" % arg)
	f = open(arg, 'rb')
	result = hashlib.md5(f.read()).hexdigest()
	f.close()
	return result.decode('utf-8')

@jinja2.contextfunction
def file_stat(context, arg):
	logging.info("File (%s) stat" % arg)
	return os.stat(arg)

@jinja2.contextfunction
def getarg(context):
	logging.info("Get arguments")
	global arguments
	return arguments

def main(options):
	logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

	global arguments
	arguments = ""
	if (options.arg):
		exec("%s = %s" % ("tmp",  options.arg))
		arguments = tmp
	
	logging.info("Load Environment")
	env = Environment(loader=FileSystemLoader(".", encoding='utf-8'), extensions=["jinja2.ext.do",])
	env.globals.update(load_csv = load_csv)
	env.globals.update(load_xml = load_xml)
	env.globals.update(load_sqlite = load_sqlite)
	env.globals.update(load_text = load_text)
	env.globals.update(le = le)
	env.globals.update(log = log)
	env.globals.update(file_md5 = file_md5)
	env.globals.update(file_stat = file_stat)
	env.globals.update(getarg = getarg)


	if (options.format == "odt"):
		logging.info("Read ODT template")
		engine = secretary.Renderer(environment=env)
		template = open(options.template, 'rb')
		logging.info("Template rendering...")
		output_data = engine.render(template)
		logging.info("Template rendering done")
		output_file = open(options.output, 'wb')
		output_file.write(output_data)
		output_file.close()
		logging.info("Done")

	elif (options.format == "text"):
		logging.info("Read TEXT template")
		template = env.get_template(options.template)
		logging.info("Template rendering...")
		output_data = template.render( )
		logging.info("Template rendering done")
		output_file = open(options.output, 'wb')
		output_file.write(output_data.encode('utf8'))
		output_file.close()
		logging.info("Done")
	else:
		logging.info("Error format")


parser = OptionParser(version='0.4', description='Python programm to processing template')
parser.add_option("-t", "--template", help="File with template", type="string")
parser.add_option("-o", "--output", help="File to save data", type="string")
parser.add_option("-f", "--format", help="Template file format", type="choice", choices=['text', 'odt',], default='text')
parser.add_option("-a", "--arg", help="Set arg valiable in python like syntax", type="string", default="")



if __name__ == "__main__":
	(options, args) = parser.parse_args()
	if (not options.template) or (not options.output):
		parser.error("set options -t and -o")
		parser.print_help()

	main(options)


