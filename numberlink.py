'''Benjo Fish'''
import time
import sys
from os import listdir,system
from search import *

#################  
# Problem class #
#################

class NumberLink(Problem):
	def __init__(self, init):
		self.letter=[]
		self.end=[]
		self.start=[]
		self.parent=[]
		self.createMap(init)
		self.n=len(self.letter)
		pass
	
	def goal_test(self, state):
		n=self.n
		i=0
		maap=state[1]
		for (letter,ligne,col) in self.end:
			for diir in directions:
				newL=ligne+diir[1]
				newC=col+diir[0]
				if((inBounds(maap,[newL,newC])) and (maap[newL][newC]==letter)):
					i=i+1
					break
		if(i==n):                        
			return True
		else:
			return False
	
	def successor(self, state):
		successors = []
		currentLetter = state[0][0][0]
		if(possible(state[1],self.start,self.end,list(state[0][0]),currentLetter) and possible2(state[1],state[0][1],self.end,self.start)):
						grid = tupleToList(state[1])
						currentStartPoint = state[0][1]
						for elem in self.end:
								if elem[0] == currentLetter:
										currentEndPoint = (elem[1],elem[2])
										break 		
						choice = chooseLetter(grid,currentLetter,currentStartPoint,currentEndPoint,state[0][0],self.start,self.end)			
						currentLetter = choice[0][0]
						currentStartPoint = choice[1]
						currentEndPoint = choice[2]		
						for diir in directions:
								nextline = currentStartPoint[0]+diir[1]
								nextcol = currentStartPoint[1]+diir[0]
								if(pathExists(grid,[nextline,nextcol],currentEndPoint) and grid[nextline][nextcol]=='.'):
										grid[nextline][nextcol] = currentLetter
										if(possible(grid,self.start,self.end,list(choice[0]),currentLetter) and possible2(grid,(nextline,nextcol),self.end,self.start)):
											nextState = ((choice[0],(nextline,nextcol)),listToTuple(grid))
											successors.append( (diir,nextState  ) )
										grid[nextline][nextcol] = '.'
				#self.parent=listToTuple(grid)
						return tuple(successors)
		print("None")				
		return ()

	def createMap(self,path):
		mapL=[]
		endLetter=[]
		letter=[]
		startLetter=[]
		f=open(path,'r')
		ligne=0
		for line in f:
			mapL2=[]
			colonne=0
			for col in line:
				if(col!= '\n'):
					mapL2.append(col)
				if(col!='.' and col!='\n'):
					if col in letter:
						endLetter.append((col,ligne,colonne))
					else:
						letter.append(col)
						startLetter.append((col,ligne,colonne))
				colonne=colonne+1
			mapL.append(tuple(mapL2))
			ligne=ligne+1
		self.end=endLetter
		self.letter=letter
		self.start=startLetter
		line = startLetter[0][1]
		col = startLetter[0][2]
		self.initial=((tuple(letter),(line,col)),tuple(mapL))
		f.close
		#print(startLetter)
		#print(endLetter)



###################### 
# Auxiliary function #
######################

directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]

def tupleToList(yuple):
	llist = []
	for line in yuple:
		llist.append(list(line))
	return llist

def listToTuple(List):
	Tuple = []
	for line in List:
		Tuple.append(tuple(line))
	return tuple(Tuple)	

def checkEnd(currentPoint,endPoint):
	for diir in directions:
		if ((currentPoint[0]+diir[1] == endPoint[0]) and (currentPoint[1]+diir[0] == endPoint[1])):
			return True
	return False	

def chooseLetter(grid,currentLetter,currentStartPoint,currentEndPoint,listLetter,listStartPoint,listEndPoint):	
	if (not checkEnd(currentStartPoint,currentEndPoint)):
		return (tuple(listLetter),currentStartPoint,currentEndPoint)		 
	else:
		listLetter = list(listLetter)
		listLetter.remove(currentLetter)
		for elem in listStartPoint:
			if elem[0] == listLetter[0]:
				startPoint = (elem[1],elem[2])
				break
		for elem in listEndPoint:
			if elem[0] == listLetter[0]:
				endPoint = (elem[1],elem[2])
				break		
		return (tuple(listLetter),startPoint,endPoint)	
			
def numberDot(grid, col):
		i=0
		for e in grid:
			if(e[col]=='.'):
				i=i+1
		return i

def lVr(grid, currentPos,endP,startP):
		lC=currentPos[0]
		cC=currentPos[1]
		i=0
		for (letterS,lS,cS),(letterE,lE,cE) in zip(startP,endP) :
			if ((cS<cC and cE>cC) or (cS>cC and cE<cC)):
				i=i+1
		return i

def possible2(grid,currentPos,end,start):
	nDot=numberDot(grid,currentPos[1])
	nLVR=lVr(grid,currentPos,end,start)
	if(nDot<nLVR):
		return False
	return True

def possible(grid,start,end,listL,currentLetter):
		if(len(listL)!=0):
			listL.remove(currentLetter)
			for e in listL:
				for elem in start:
					if elem[0] == e:
						startP = (elem[1],elem[2])
						break
				for elem in end:
					if elem[0] == e:
						endP = (elem[1],elem[2])
						break
				if( not pathExists(grid, startP,endP)):
					return False
			return True
			
		return False	

def pathExists(grid, start, end):
	visited = [ [0 for j in range(0, len(grid[0]))] for i in range(0, len(grid)) ]
	ok = pathExistsDFS(grid, start, end, visited)
	return ok

def pathExistsDFS(grid, start, end, visited):
	for d in directions:
		i = start[0] + d[0]
		j = start[1] + d[1]
		next = [i, j]
		if i == end[0] and j == end[1]:
			return True
		if inBounds(grid, next) and grid[i][j] == '.' and not visited[i][j]:
			visited[i][j] = 1
			exists = pathExistsDFS(grid, next, end, visited)
			if exists:
				return True
	return False

def inBounds(grid, pos):
	return 0 <= pos[0] and pos[0] < len(grid) and 0 <= pos[1] and pos[1] < len(grid[0])

def printState(state):
	for e in state[1]:
		line=''.join(e)
		print(line)
	print("")
#####################
# Launch the search #
#####################

problem=NumberLink(sys.argv[1])

#example of bfs search
node=depth_first_graph_search(problem)
#example of print
path=node.path()
path.reverse()
for n in path:
	printState(n.state) #assuming that the __str__ function of states output the correct format

