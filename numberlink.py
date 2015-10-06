'''NAMES OF THE AUTHOR(S): TODO'''
"YO"
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
                self.createMap(init)
	
	def goal_test(self, state):
		i=0
		for e in state[1]:
			if '.' in e:
				return False
		return True
    
	def successor(self, state):
		pass

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
		self.initial=([0,0],tuple(mapL))
		self.end=tuple(endLetter)
		self.letter=letter
		self.start=tuple(startLetter)
		print(startLetter)
		print(endLetter)
                                

###################### 
# Auxiliary function #
######################

directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]

def tupleToList(yuple):
	llist = []
	for line in yuple:
		llist.append(list(line))
	return llist

def ListToTuple(List):
	Tuple = []
	for line in List:
		Tuple.append(tuple(line))
	return tuple(Tuple)	

def checkStart(parent,child):
	li=0
	col=0
	for line in parent:
		for elem in line:
			if parent[li][col] != child[li][col]:
				return (li,col)
			col=col+1
		li=li+1
	return 'same'

def checkEnd(currentPoint,endPoint,letter):
	for diir in directions:
		if ((startpoint[0]+diir[0] == endPoint[0]) and (startpoint[1]+diir[1] == endPoint[1])):
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

#####################
# Launch the search #
#####################


problem=NumberLink(sys.argv[1])

#example of bfs search
#node=depth_first_graph_search(problem)
#example of print
#path=node.path()
#path.reverse()
#for n in path:
#        print(n.state) #assuming that the __str__ function of states output the correct format

