print("begin of work")

helloString = ""
fReadName = 'r.txt'
fWriteName = 'w.txt'

fileToWrite = open(fWriteName, 'w')
fileToRead = open(fReadName, 'r')

#with open('r.txt') as fileToRead:
helloString = fileToRead.read(100)
fileToRead.seek(0,0)
for line in fileToRead:
	print(line)
#f.closed
fileToWrite.write(helloString)

fileToRead.close()
fileToWrite.close()

print("end of work")
