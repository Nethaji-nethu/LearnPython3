def printASCIITable():
	START = 32
	STOP = 126
	for ascii_val in range(START,STOP+1):
		print(ascii_val, " " , chr(ascii_val))
printASCIITable()