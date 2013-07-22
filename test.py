#!/bin/python
import Modules

def main():
	a = Modules.reference_mapper.reference_mapper()
	a.insert_references("..")
	#a.find_resources("../..")

if __name__ == "__main__":
	main()
