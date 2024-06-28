f=open("samplefile1.txt","r+")
#using tell function to detect current position of cursor
print(f.tell())
#moving the cursor position to 5 postion using seek() then return its postion using tell function

f.seek(5)
print(f.tell())
f.close()