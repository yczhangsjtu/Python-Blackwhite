from Tkinter import *

root = Tk()

def gamestart():
	global array, side, started
	side = 1
	array = []
	for i in range(15):
		array.append([0]*15)
	started = True
	draw()

def gameexit():
	quit()

def draw():
	canvas.delete(ALL)
	canvas.create_rectangle(0,0,600,600,fill="yellow")
	for i in range(1,15):
		canvas.create_line(0,40*i,600,40*i)
		canvas.create_line(40*i,0,40*i,600)
	for x in range(15):
		for y in range(15):
			if array[x][y] == 1:
				canvas.create_oval(x*40+2,y*40+2,x*40+38,y*40+38,fill="black")
			elif array[x][y] == 2:
				canvas.create_oval(x*40+2,y*40+2,x*40+38,y*40+38,fill="white")
				
def mouseclick(event):
	if not started: return
	global side, array
	x, y = event.x, event.y
	x = x / 40
	y = y / 40
	if x >= 0 and x < 15 and y >= 0 and y < 15 and array[x][y]==0:
		array[x][y] = side
		side = 3 - side
		work(x,y)
	draw()

def work(x,y):
	for dirx in range(-1,2):
		for diry in range(-1,2):
			count = 0
			bx, by = x, y
			if dirx == 0 and diry == 0: continue
			while True:
				bx = bx + dirx
				by = by + diry
				if bx < 0 or bx >= 15 or by < 0 or by >= 15:
					break
				if array[bx][by] == 0:
					break
				if array[bx][by] == array[x][y]:
					if count > 0:
						xx, yy = x, y
						for i in range(count):
							xx = xx + dirx
							yy = yy + diry
							array[xx][yy] = array[x][y]
					break
				else:
					count += 1
				
	
started = False
array = []
for i in range(15):
	array.append([0]*15)
side = 1
rframe = Frame(root)
start = Button(rframe,text="Start",command=gamestart)
exit  = Button(rframe,text="Exit",command=gameexit)
canvas = Canvas(root,width=600,height=600)

start.pack(side=BOTTOM)
exit.pack(side=BOTTOM)
canvas.pack(side=LEFT)
rframe.pack(side=LEFT)
draw()

canvas.bind("<Button-1>",mouseclick)

root.mainloop()
