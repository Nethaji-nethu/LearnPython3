try :
	input_number = int(input('Enter a number : '))
	if input_number % 2 == 0:
		print('Number is even ')
	else :
		print('Number is Odd ')
except:
	print('Integer number only !!')