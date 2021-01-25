myfile=open("new.txt", "w+", "a+")
for i in range(3):
    myfile.write("Banana %d\r\n" % (i+1))
contents = myfile.read()
print(contents)
myfile.close()
import os
os.remove(./myfile.txt)