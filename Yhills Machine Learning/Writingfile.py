#opening of file
a=open("sample.txt","a+")
#writing a single word in file
a.write('a')
#writing a single line in file
a.write("hello")
#writing a 'n' number of lines in file
l='''hi my name
is 
aditya das
'''
a.writelines(l) 
a.close()