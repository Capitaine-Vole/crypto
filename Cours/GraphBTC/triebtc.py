import json

from filemanagement import *

all = readFile(getFromConfig('dataFile'))

count = len(open(getFromConfig('dataFile')).readlines())

print("Number of lines: " + str(count))


total = {}

total = all.split('\n')

total.remove('')

print(type(total))


print(total)