#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

# if os.path.isfile(myfilename):
#   print("yay, I have a file")
#   if sky == blue:
#     print('yay the sky is blue')
# else:
#   print ('boo, no files for me')

with open(myfilename, 'r') as file_handle:

    #mylist = [] #new

    for line in file_handle.readlines():

        #mylist.clear() #new

        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')

        values = ('[%s]' %', '.join(map(str,values)))

        #New
        #for idx, item in enumerate(values):
            #print(values[idx])
            #For i in range(len(values)):     #issues with i
            #x=values[idx]
            #if type(values[idx]) == 'float':
            #    x = float(values[idx])

            #elif type(values[idx]) == 'str':
            #    x = str(values[idx])

            #elif type(values[idx]) == 'int':
            #    x = int(values[idx])
            #else:
            #    x = values[idx]
        #New
        #mylist.insert(idx,x)
        #print(mylist)

        print(values)

        #for value in values:
            # for homework:
            # identify what type of data each value is, and cast it
            # to the appropriate type, then print the new, properly-typed
            # list to the screen.
            # I.e. ['0.04741', '0.00', '11.930', '0', '0.5730', '6.0300', '80.80', '2.5050', '1', '273.0', '21.00', '396.90', '7.88', '11.90']
            # becomes: [0.04741, 0.0, 11.93, 0, 0.573, '6.03, 80.8, 2.505, 1, 273.0, 21.0, 396.90, 7.88, 11.90]
            #print(float(value))
    print('finished!')
