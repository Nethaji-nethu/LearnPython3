def writeToFile(filename,text):
	with open(filename,'w') as fw:
		fw.write(text)

def appendToFile(filename,text):
	with open(filename,'a') as fa:
		fa.write(text)

def readFromFile(filename):
	with open(filename,'r') as fr:
		return fr.read()

if __name__ == '__main__':
	filename = input('enter the filename : ')
	writeToFile(filename, 'Hello!\n')
	appendToFile(filename, 'Goodbye!\n')
	assert readFromFile(filename) == 'Hello!\nGoodbye!\n'
	