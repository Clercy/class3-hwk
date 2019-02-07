#!/usr/bin/env python







import os



myfilename = "housing.data.txt"

#if os.path.isfile(myfilename):

#	print("yay, I have a file")

#else:

#	print ('boo, no files for me')

with open(myfilename, 'r') as file_handle:

	#line = file_handle.readline()

	#for line in file_handle.read():

	for line in file_handle.readlines():

		line_clean = line.replace('   ', ' ').replace('  ', ' ')

		#line_clean = line_clean.strip()

		line_clean = line.replace('\n','')
		#line_clean = line.replace('[','')
		values = line_clean.split(' ')

		print(values)

		for value in values:

			print(float(value))



#for homework idenntify whattype of data each value is

#and cast it to appropriate type then print the new

#properly types list to screen

#goal is to see numbers like bash: y: command not found



	#	print(line_clean.split(' '))

		#print(line)

	print('Finished')
