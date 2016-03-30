#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import unittest
from pytemplate import *

class HelloworldTestCase(TestCase):
	def test_loadcsv(self):
		out = load_csv(None, "examples/database2.csv")
		self.assertNotEqual(out, None)
		self.assertEqual(len(out), 28)
	def test_loadxml(self):
		out = load_xml(None, "examples/database1.xml")
		self.assertNotEqual(out, None)
		self.assertEqual(out.find('name').text, u"Программное обеспечение")
	def test_loadxml(self):
		out = load_sqlite(None, "examples/database3.sqlite")
		self.assertNotEqual(out, None)
		self.assertEqual(len(out.execute("select * from Album").fetchall()), 347)
	def test_loadtext(self):
		out = load_text(None, "examples/database4.txt")
		self.assertNotEqual(out, None)
		self.assertEqual(len(out), 63)
	def test_le(self):
		out = le(None, "AAAA_BBBB&CCCC")
		self.assertNotEqual(out, None)
		self.assertEqual(out, "AAAA\_BBBB\&CCCC")
	def test_log(self):
		out = log(None, "Test Log 1234567890-=\`qwertyuiop[]asdfghjkl;'zxcvbnm,./")
		self.assertNotEqual(out, None)
		self.assertEqual(out, "")
	def test_filemd5(self):
		out = file_md5(None, "examples/database3.sqlite")
		self.assertNotEqual(out, None)
		self.assertEqual(out, "9ebece0dad4a7ee91b9ce97a12c04e26")
	def test_filestat(self):
		out = file_stat(None, "examples/database3.sqlite")
		self.assertNotEqual(out, None)
		self.assertEqual(out.st_size, 1067008)

if __name__ == '__main__':
    unittest.main()

