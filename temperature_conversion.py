import sys
try:
	choice = int(input('1. Degree Celsius to Fahrenheit\n2. Fahrenheit to Degree Celsius\n'))
	if choice == 1:
		input_temp = float(input('Enter the temprature in Degree Celsius: '))
		print('Degree Celsius = {}\t=>\tFahrenheit = {}'.format(input_temp, 32 + input_temp*(9/5) ))
	elif choice ==2:
		input_temp = float(input('Enter the temprature in Fahrenheit: '))
		print('Fahrenheit = {}\t=>\tDegree Celsius = {}'.format(input_temp, (input_temp-32)*(5/9) ))
	
except :
	print('Only enter the numeric value. ')
	sys.exit(1)
