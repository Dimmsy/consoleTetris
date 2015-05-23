def tetris():
	import random
	from time import sleep

	#Game constants
	gameUpdateRate = 1 #seconds between frames

	#Field width and height
	global w, h
	w, h = 10, 14

	#Symbols
	global empty, fill
	empty = '_'
	fill = 'O'

	#Tetrinos
	global s_block
	s_block = [[0,0],[1,0],[1,-1],[2,-1]]


	#Create field
	staticField = [None]*h
	for i in range(h):
		staticField[i]=[empty]*10

	#Create block
	activeBlock = Tetrino()

	#----------------
	#---- Game Loop -
	#----------------
	while 1:
		activeBlock.update()
		dynamicField = updateField(staticField,activeBlock)
		#print field to console
		printField(dynamicField)
		print ''
		#wait a 'frame'
		sleep(gameUpdateRate)

################## CLASSES #################
class Tetrino:
	def __init__(self):
		#Define shape
		self.shape = s_block
		#spawn at top of board
		self.x = 3
		self.y = 0
	def update(self):
		self.y += 1

################# FUNCTIONS ################
	#Updates field with block position
def updateField(field,block):
	#Welp, gotta do this to copy over static field without editing it
	outField = []
	for i in range(h):
		outField.append([])
		for j in range(w):
			outField[i].append(field[i][j])
			
	#Draw field with block
	for coord in block.shape:
		if block.y+coord[1]>=0 and block.y+coord[1]<=h-1:
			outField[block.y+coord[1]][block.x+coord[0]]=fill
	return outField
	
	# Prints field to console
def printField(field):
	for i in range(len(field)):
		row = ''
		for j in range(len(field[i])):
			row = row+field[i][j]
		print row

################## Main function ###########
if __name__ == '__main__':
	tetris()

