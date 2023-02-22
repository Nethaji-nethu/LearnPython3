def getChessSquareColor(row,column):
	if not ( row in range(0,8) and column in range(0,8)):
		return ''
	else:
		if (row+column) % 2 == 0:
			return 'white'
		else:
			return 'black'

assert getChessSquareColor(0, 0) == 'white'
assert getChessSquareColor(1, 0) == 'black'
assert getChessSquareColor(0, 1) == 'black'
assert getChessSquareColor(7, 7) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''