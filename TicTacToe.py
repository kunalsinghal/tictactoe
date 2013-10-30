from graphics import *

print "This is a Tic-tac-toe game. But there is a slight change. Instead of cross and circle,"
print "we are going to have red and green colors. enjoy!"

size = winp = 0
while True:
	size = int(raw_input("Enter the size of the tic tac toe board you wanna play: "))
	winp = int(raw_input("Enter the winning parameter k: "))
	if winp > size : 
		print "size of board cannot be less than winning parameter, try again."
		continue
	break

boxSize = min(100,int(750/size))

l = [[0 for i in range(size)]for j in range(size)]

def Rect(x,y):
	return Rectangle(Point(x,y+boxSize),Point(x+boxSize,y))

rec = [[Rect(i*boxSize,j*boxSize) for i in range(size)]for j in range(size)]

win = GraphWin("Tic Tac Toe - SkyRyders",size * boxSize,size * boxSize)
win.setCoords(0,size * boxSize,size * boxSize,0)

for x in rec: 
	for y in x:
		y.draw(win)
		
def probe(x,y,n):
	if x >= size or y>=size or x<0 or y<0: 
		return False
	return n == l[x][y]
	
def highlight(color):
	for x in range(size):
		for y in range(size):
			n = l[x][y]
			if n == 0 : continue
			flag = True
			for i in range(winp):
				flag = probe(x+i,y,n)
				if flag == False:
					break
			if flag : 
				for i in range(winp):
					rec[x+i][y].setFill(color)
				return 0
		
			flag = True
			for i in range(winp):
				flag = probe(x+i,y+i,n)
				if flag == False:
					break
			if flag : 
				for i in range(winp):
					rec[x+i][y+i].setFill(color)
				return 0
			
			flag = True
			for i in range(winp):
				flag = probe(x,y+i,n)
				if flag == False:
					break
			if flag : 
				for i in range(winp):
					rec[x][y+i].setFill(color)
				return 0
				
			flag = True
			for i in range(winp):
				flag = probe(x-i,y+i,n)
				if flag == False:
					break
			if flag : 
				for i in range(winp):
					rec[x-i][y+i].setFill(color)
				return 0
	return 0

	
def check():
	for x in range(size):
		for y in range(size):
			n = l[x][y]
			if n == 0 : continue
			flag = True
			for i in range(winp):
				flag = probe(x+i,y,n)
				if flag == False:
					break
			if flag : return n
			
			flag = True
			for i in range(winp):
				flag = probe(x+i,y+i,n)
				if flag == False:
					break
			if flag : return n
			
			flag = True
			for i in range(winp):
				flag = probe(x,y+i,n)
				if flag == False:
					break
			if flag : return n

			flag = True
			for i in range(winp):
				flag = probe(x-i,y+i,n)
				if flag == False:
					break
			if flag : return n
	return 0


moves = 0
turn = 1			
 
while moves < size * size : 
	p = win.getMouse()
	y = int(p.getX() / boxSize) 
	x = int(p.getY() / boxSize) 
	if l[x][y] > 0: 
		continue
	l[x][y] = turn 
	color = "Red" if turn == 1 else "Green"
	rec[x][y].setFill(color)
	turn = 3 - turn 
	status = check()
	if status == 1 : 
		print "Player 1 wins"
		highlight("Dark Red")
		break
	if status == 2:
		print "Player 2 wins"
		highlight("Dark Green")
		break
	moves += 1 

if moves == size*size :
	print "Draw match"
	for x in rec:
		for y in x:
			y.setFill("Blue")
win.getMouse()