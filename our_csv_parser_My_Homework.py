#!/usr/bin/env python

def checkintfloat (s):

    try:
        return int (s)
    except ValueError:
        return  float (s)


myfilename = "housing.data.txt"

with open(myfilename, 'r') as file_handle:

    mylist = []

    for line in file_handle.readlines():

        mylist.clear()

        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')

        for idx, item in enumerate(values):

            y = values[idx]
            y = y.replace("'","")
            #print(type(checkintfloat(y)))
            y = checkintfloat(y)

            #print(y)

            #print(type(y)) #shows all types for the list elements
            mylist.insert(idx,y)

        #for idx in range(len(values)):
        #for i in range(len(values)):     #issues with i
        	   #print(values[idx]      #x=values[idx]

        #print(mylist)
        #print('[%s]' % ', '.join(map(str, mylist)))



        #[[mylist[jdx][idx] for jdx, row in enumerate(mylist) for idx, column in enumerate(mylist[0])

        print(mylist)
        #print(values)






        #for value in values:
            # for homework:
            # identify what type of data each value is, and cast it
            # to the appropriate type, then print the new, properly-typed
            # list to the screen.
            # I.e. ['0.04741', '0.00', '11.930', '0', '0.5730', '6.0300', '80.80', '2.5050', '1', '273.0', '21.00', '396.90', '7.88', '11.90']
            # becomes: [0.04741, 0.0, 11.93, 0, 0.573, '6.03, 80.8, 2.505, 1, 273.0, 21.0, 396.90, 7.88, 11.90]
            #print(float(value))

		#print('finished!')
