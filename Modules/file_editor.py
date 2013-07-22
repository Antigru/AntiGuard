#!/bin/python
import re
import os
import sys

def insert_text(old_file,new_file,regex,string_map):


        with open(old_file,'r') as o:
                with open(new_file,'w') as n:
                        for line in o:
                                finder = re.search(regex,line)
                                if finder:
                                  try:
                                         temp = line[:-1] + " #! " + string_map[finder.group(1)] + '\n'
                                         n.write(temp)
                                  except KeyError:
                                         n.write(line)                                    
                                  except: print "Unexpected error:", sys.exc_info()[0]
                                else:
                                  n.write(line)
	os.remove(old_file)
	os.rename(new_file,old_file)

