filename = input('Enter text file name: ')

file_object = open(filename + '.txt','r')
lines = file_object.readlines()
for line in lines:
	print(line)
input("Press enter to exit")