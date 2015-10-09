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
		self.letter=[] #list of all different letters into the grid
		self.end=[] #list of cooordinates of all ending letters
		self.start=[] #list of coordinates of all starting letters
		self.createMap(init)
		self.n=len(self.letter) # number of different letters into the grid
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
	
	def successor(self, state): #state = (  ( (currentLisLetter),(currentPointLine,currentPointCol) ),(grid)  )
		successors = []
		currentListLetter = state[0][0]
		currentLetter = state[0][0][0]
		currentStartPoint = state[0][1]
		grid = tupleToList(state[1])
		for elem in self.end:
			if elem[0] == currentLetter:
				currentEndPoint = (elem[1],elem[2])
				break 		
		choice = chooseLetter(grid,currentLetter,currentStartPoint,currentEndPoint,currentListLetter,self.start,self.end)
		currentListLetter = choice[0] #ChooseLetter check if we need to change letter or not.			
		currentLetter = choice[0][0]  
		currentStartPoint = choice[1]
		currentEndPoint = choice[2]		
		for diir in directions:
			nextline = currentStartPoint[0]+diir[1]
			nextcol = currentStartPoint[1]+diir[0]
			if(pathExists(grid,[nextline,nextcol],currentEndPoint) and grid[nextline][nextcol]=='.'):
				grid[nextline][nextcol] = currentLetter
				if(possible(grid,self.start,self.end,list(currentListLetter),currentLetter,(nextline,nextcol))):
					nextState = ((currentListLetter,(nextline,nextcol)),listToTuple(grid))
					successors.append( (diir,nextState  ) )
				grid[nextline][nextcol] = '.'
		return tuple(successors)

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

def possible(grid,start,end,listL,currentLetter,currentPos):
	for letter in listL:
		for elem in start:
			if elem[0] == letter:
				startP = (elem[1],elem[2])
				break
		for elem in end:
			if elem[0] == letter:
				endP = (elem[1],elem[2])
				break
		if(letter != currentLetter):		
			if( not pathExists(grid, startP,endP)):
				return False
		else:
			currentStartPoint = startP
			currentEndPoint = endP
	if(isCycle(grid,currentLetter,currentStartPoint,currentEndPoint,currentPos)):
		return False
	return True	

def isCycle(grid,currentLetter,startP,endP,currentPos):
	curL=currentPos[0]
	curC=currentPos[1]
	count=0 
	if curL+1<len(grid) and grid[curL+1][curC]==currentLetter and ((curL+1,curC)!=startP and (curL+1,curC)!=endP) :
		count+=1
	if curL>0 and grid[curL-1][curC]==currentLetter and ((curL-1,curC)!=startP and (curL-1,curC)!=endP) :
		count+=1      
	if curC+1<len(grid[curL]) and grid[curL][curC+1]==currentLetter and ((curL,curC+1)!=startP and (curL,curC+1)!=endP): 
		count+=1
	if curC>0 and grid[curL][curC-1]==currentLetter and ((curL,curC-1)!=startP and (curL,curC-1)!=endP):
		count+=1
       
	if count>=2:	
		return True
	else:
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
start_time = time.time()  
problem=NumberLink(sys.argv[1])

#example of bfs search
node=breadth_first_graph_search(problem)
#node=depth_first_graph_search(problem)
#example of print
path=node.path()
path.reverse()
for n in path:
	printState(n.state) #assuming that the __str__ function of states output the correct format




interval = time.time() - start_time  
print('Total time in seconds:', interval )
