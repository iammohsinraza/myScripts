import os
currentPath = os.getcwd()
file = os.listdir(currentPath)
print(file[1])
workFile = open(file[1],'r')
lines = workFile.readlines()
workFile.close()

workFile = open(file[1],'w')
for line in lines:
    workFile.write(char+line)
workFile.close()
