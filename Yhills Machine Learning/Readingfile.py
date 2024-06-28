#opening a new file
#it will through error if it already created once
'''
a=open("samplefile1.txt","x")
a.close()
'''
f=open("samplefile1.txt","r+")
#reading the entire file 
print(f.read())

#reading the specific character
print(f.read(3))

#reading single line
print(f.readline())

#reading specific lines
print(f.readline(3))

#reading entire lines in file
print(f.readlines())

#closing the file
f.close()