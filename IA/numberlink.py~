#BENJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
	#Jewish
import time
import sys
from os import listdir,system
from search import *

#################  
# Problem class #
#################

class NumberLink(Problem):
    def __init__(self, init):
            self.createMap(init)
            print(self.goal_test(self.initial))
            pass
	
    def goal_test(self, state):
            i=0
            for e in state[0]:
                if '.' in e:
                    return False
            return True
    
    def successor(self, state):
	    pass

    def createMap(self,path):
            mapL=[]
            mapLetter=[]
            f=open(path,'r')
            y=0
            for line in f:
                    mapL2=[]
                    x=0
                    for col in line:
                        if(col!= '\n'):
                                mapL2.append(col)
                        if(col!='.' and col!='\n'):
                            mapLetter.append((col,x,y))
                        x=x+1
                    mapL.append(tuple(mapL2))
                    y=y+1
            print(mapL)
            print(mapLetter)
            self.initial=(tuple(mapL),tuple(mapLetter))


###################### 
# Auxiliary function #
######################

directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]

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

