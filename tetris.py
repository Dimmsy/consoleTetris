def tetris():
	import random
	from time import sleep

	#Game constants
	gameUpdateRate = 1 #seconds between frames

	#Field width and height
	w, h = 10, 14

	#Symbols
	empty = '_'
	block = 'O'

	#Create field
	field = [None]*h
	for i in range(h):
		field[i]=[empty]*10

	#----------------
	#---- Game Loop -
	#----------------
	while 1:
		#print field to console
		printField(field)
		#wait a 'frame'
		sleep(gameUpdateRate)

class Tetrino:
	def __init__(self):
		#Define shape
		#spawn at top of board
		return
	

def printField(field):
	for i in range(len(field)):
		row = ''
		for j in range(len(field[i])):
			row = row+field[i][j]
		print row

if __name__ == '__main__':
	tetris()

