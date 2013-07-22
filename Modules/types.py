#!/usr/bin/python
import re
import os.path

class file:

	def __init__(self,name,path):
		self.name = name
		self.path = path
			
	def rename(self,new_name):	
		self.name = new_name

class directory(file):

	self.contents = {}


class smali_file(file):

	self.variables = []
	self.methods = []
	self.base = ''

	def parse(self):
		try:
			with open(os.path.join(self.path, self.name)) as f:
				self.find_base(f)
				self.find_variables(f)
				self.find_methods(f)
		except IOError: 
			print "file not found: " + self.path + "/" + self.name
			return -1
		except:
			print "unknown error"
			return -1
	

	def find_base(self,f):
		#.super Lflashingtools/util/a;
		
		pass

	def find_variables(self,f):
		pass

	def find_methods(self,f):
		pass

	def rename_base(self,new_name):
		pass

	def rename_variable(self,old,new):
		pass

	def rename_method(self,old,new):
		pass


