



mylist = [] #new
mylist.clear() #new

values = [1, 2.05, 0.016]

i = 0

#for idx, item in enumerate(values):
print(values[idx])

i=0
For i in range(len(values)):

    if type(values[i]) == 'float':
          x = float(values[i])
    elif type(values[i]) == 'str':
          x = str(values[i])
    elif type(values[i]) == 'int':
          x = int(values[i])
    else:
        x = values[i]
    i += 1
mylist.insert(i,x)
print('mylist now')
print(mylist)
