#!/bin/python
import os
import re
import sys
import file_editor

class reference_mapper:
	

	def __init__(self):
		self.string_mapping = {}
		self.mapping = {}
		self.res_directory = ""
		self.strings_parse = re.compile(r'string.+?name=.(\w+?).>(.+?)<')
		self.public_parse = re.compile(r'name=.(\w+?).\sid=.(\w+?)"')	
		self.address_parse =  re.compile(r'(0x([0-9]|[a-f]){8})')
		self.res_directory = ""
			
	def find_resources(self,file_path):
		self.directory_list = os.listdir(file_path)

		for entry in self.directory_list:
			try:
				with open(os.path.join(file_path,  entry, "AndroidManifest.xml")):
					self.res_directory = entry
			except IOError: pass
				
		if self.res_directory == "": 
			print "Could not find AndroidManifest.xml. Exiting"
			return -1 
	
		try:
			with open(os.path.join(file_path,self.res_directory,"res","values","strings.xml")) as f:
				for line in f:
					pair = self.parse_string_xml(line)
					if pair != -1:
						#print pair	
						self.string_mapping[pair[0]] = pair[1]
						
		except IOError: pass

		try:
			with open(os.path.join(file_path,self.res_directory,"res","values","public.xml")) as f:
				for line in f:
					#print line
					pair = self.parse_public_xml(line)
					#print pair
					if pair != -1: 
						try:
							self.mapping[pair[1]] = self.string_mapping[pair[0]]
						except KeyError: pass
		except: 
    			print "Unexpected error:", sys.exc_info()[0]	
	
		#print self.mapping
		return self.mapping
		
	def parse_string_xml(self,xml_line): 
		results = re.search(self.strings_parse,xml_line)	
		if results:
			return (results.group(1),results.group(2))
		else: 
			return -1	
	
	def parse_public_xml(self,xml_line):
		results = re.search(self.public_parse,xml_line)
		if results:
			return (results.group(1),results.group(2))			
		else:
			return -1		

	def insert_references(self,file_path):
		temp = ''
		new_path = os.path.join(file_path, self.res_directory, "smali")
		string_map = self.find_resources(file_path)
		#use os.walk(dir), print out first and third values for return:
		#i.e. for i,j,k in os.walk(dir): 
		#	print i
		#	print k
		for i,j,k in os.walk(new_path):
			for file in k:
				old_file = os.path.join(i,file)
				new_file = os.path.join(i,file) + "-new"
				file_editor.insert_text(old_file,new_file,self.address_parse,string_map)				
