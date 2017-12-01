file = open('hello.txt','r')
data = file.readlines()
file.close()
data[1] = 'A new line with the replace of c\n'
file = open('hello.txt','w')
for line in data:
    file.write(line)
file.close()
input()
