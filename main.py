#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jinja2
from jinja2 import Environment, PackageLoader, FileSystemLoader, BaseLoader, nodes
from jinja2.ext import Extension
import csv
import sys
import logging
from optparse import OptionParser

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

def main(options):
	logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
	logging.info("Read template")
	env = Environment(loader=FileSystemLoader(".", encoding='utf-8'))
	template = env.get_template(options.template)

	env.globals.update(load_csv = load_csv)

	#logging.info("Read CSV")
	#csvfile = open(options.csv, 'rt')
	#csvreader = UnicodeDictReader(csvfile)
	#csvdata = list(csvreader)
	#csvfile.close()
	#logging.info("Read %d lines" % len(csvdata))

	logging.info("Template rendering...")
	output_data = template.render( )

	logging.info("Template rendering done")

	logging.info("Write output data...")
	output_file = open(options.output, 'wb')
	output_file.write(output_data.encode('utf8'))
	output_file.close()
	logging.info("Done")

parser = OptionParser(version='0.1', description='Python programm to processing template')
#ls.add_param("-l", "--long", help="list in long format", default=False, action="store_true")
parser.add_option("-t", "--template", help="File with template", type="string")
#parser.add_option("-c", "--csv", help="File with data in CSV format", type="string")
parser.add_option("-o", "--output", help="File to save data", type="string")


if __name__ == "__main__":
	parser.print_help()
	(options, args) = parser.parse_args()
	if (not options.template) or (not options.output):
		parser.error("set options -t and -o")

	main(options)


