import random
from time import sleep

def tetris():
	#Game constants
	gameUpdateRate = .1 #seconds between frames

	#Field width and height
	global w, h
	w, h = 10, 14

	#Symbols
	global empty, fill
	empty = '_'
	fill = 'O'

	# ~~~~~ Tetrinos
	global blocks
	global sqr_block
	
	s_block = [[-1,0],[0,0],[0,-1],[1,-1]]
	z_block = [[-1,1],[0,-1],[0,0],[0,1]]
	sqr_block = [[0,0],[1,0],[0,1],[1,1]]
	li_block = [[-1,0],[0,0],[1,0],[2,0]]
	t_block = [[-1,0],[0,0],[1,0],[0,1]]
	l_l_block = [[-1,-1],[-1,0],[0,0],[1,0]]
	l_r_block =  [[1,-1],[-1,0],[0,0],[1,0]]

	blocks = [s_block,s_block,
				sqr_block,li_block,t_block,
				l_l_block,l_r_block]
	# ~~~~~~~~


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
		#Debug: random move in x
		#activeBlock.moveInX(random.randrange(-3,4), staticField)
		if random.randrange(0,4)==1:
			activeBlock.rotate('cw',staticField)

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
		self.x = 4
		self.y = 0
	def update(self,field):
		#Check collision
		print self.state
		self.moveDown(field)
	def moveDown(self,field):
		if not self.collisionBelow(1,field) and self.state == 'move':
			self.y+=1
		else: self.collideBelow()
	def rotate(self,direc,field):
		#direc = cw, ccw
		if self.shape == sqr_block: return
		if direc == 'cw':
			newShape = []
			for i in range(len(self.shape)):
				#x' = -y
				curX=self.shape[i][0]
				curY=self.shape[i][1]

				newX=-curY
				newY=curX

				newShape.append([newX,newY])
		if not self.collisionAnywhere(newShape,field):
			for i in range(len(newShape)):
				self.shape[i] = newShape[i]
			self.state = 'move'
	def collisionAnywhere(self,block,field):
		for b in block:
			if self.x+b[0] == w or self.x+b[0] < 0:
				return True
			elif self.y+b[1] >= h:
				return True
			elif self.x+b[0] >=0 and self.x+b[0]>w and self.y+b[1] >0:
				if field[self.y+b[1]][self.x+b[0]]==fill:
					return True
		return False

	def moveInX(self,move,field):
		if move == 0: return
		#inc is -1,1
		inc = move/abs(move)
		for _ in range(abs(move)):
			if not self.collisionSide(inc,field):
				self.x += inc
	def collisionSide(self,move,field):
		for block in self.shape:
			#Get pos of block
			blockx = self.x+block[0]
			blocky = self.y+block[1]
			#check if at bottom
			if blockx+move == w or blockx+move == -1:
				return True
			#check if above solid block
			elif field[blocky][blockx+move] == fill:
				return True
		return False
	def collisionBelow(self,move,field):
		#Check collision below
		for block in self.shape:
			#Get pos of block
			blockx = self.x+block[0]
			blocky = self.y+block[1]+move
			#check if at bottom
			if blocky == h:
				return True
			#check if above solid block
			elif blocky < 0: 
				if field[blocky][blockx] == fill:
					return True
	def collideBelow(self):
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
		if blockx >=0 and blockx < w and blocky >=0:
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
