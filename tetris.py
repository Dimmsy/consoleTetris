def tetris():
	import random
	from time import sleep

	#Game constants
	gameUpdateRate = .1 #seconds between frames

	#Field width and height
	global w, h
	w, h = 10, 14

	#Symbols
	global empty, fill
	empty = '_'
	fill = 'O'

	#Tetrinos
	global blocks
	
	s_block = [[0,0],[1,0],[1,-1],[2,-1]]
	sqr_block = [[0,0],[1,0],[0,1],[1,1]]
	li_block = [[0,0],[1,0],[2,0],[3,0]]

	blocks = [s_block,sqr_block,li_block]


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
		activeBlock.update(staticField)
		dynamicField = updateField(staticField,activeBlock)

		#If active block is frozen, add to static field
		if activeBlock.state == 'froze':
			#Check for game over
				#frozen tetrino is overlapping
			if checkForFailure(staticField,activeBlock):
				print 'Game over'
				return

			staticField=updateField(staticField,activeBlock)
			activeBlock = Tetrino()
			
		#print field to console
		printField(dynamicField)
		print ''
		#wait a 'frame'
		sleep(gameUpdateRate)

################## CLASSES #################
class Tetrino:
	state = 'move' # 'froze' 'hit'
	def __init__(self):
		#Define shape
		self.shape = blocks[random.randrange(len(blocks))]
		#spawn at top of board
		self.x = 3
		self.y = 0
	def update(self,field):
		#Check collision
		self.collision(field)
		print self.state
		if self.state == 'move':
			self.y += 1
	def collision(self,field):
		#Check collision below
		for block in self.shape:
			#Get pos of block
			blockx = self.x+block[0]
			blocky = self.y+block[1]
			#check if at bottom
			if blocky == h-1:
				self.collide()
			#check if above solid block
			elif field[blocky+1][blockx] == fill:
				self.collide()
	def collide(self):
		if self.state=='move': self.state='hit'
		elif self.state=='hit': self.state='froze'

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
	
def checkForFailure(field,block):
	for coord in block.shape:
		blockx = block.x+coord[0]
		blocky = block.y+coord[1]
		if field[blocky][blockx]==fill:
			return True

	return False
		
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

