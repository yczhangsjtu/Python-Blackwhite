from Tkinter import *

root = Tk()

ngrid = 8
gridsize = 50
winsize = 400
array = []

def initArray():
    global array
    array = []
    for i in range(ngrid):
        array.append([0]*ngrid)
    array[3][3] = 1
    array[4][4] = 1
    array[3][4] = 2
    array[4][3] = 2
    
def gamestart():
    global side, started
    side = 1
    initArray()
    started = True
    draw()

def gameexit():
    quit()

def draw():
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,winsize,winsize,fill="yellow")
    for i in range(1,ngrid):
        canvas.create_line(0,gridsize*i,winsize,gridsize*i)
        canvas.create_line(gridsize*i,0,gridsize*i,winsize)
    for x in range(ngrid):
        for y in range(ngrid):
            if array[x][y] == 1:
                canvas.create_oval(x*gridsize+2,y*gridsize+2,(x+1)*gridsize-2,(y+1)*gridsize-2,fill="black")
            elif array[x][y] == 2:
                canvas.create_oval(x*gridsize+2,y*gridsize+2,(x+1)*gridsize-2,(y+1)*gridsize-2,fill="white")
                
def mouseclick(event):
    if not started: return
    global side, array
    x, y = event.x, event.y
    x = x / gridsize
    y = y / gridsize
    if x >= 0 and x < ngrid and y >= 0 and y < ngrid and array[x][y]==0:
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
                if bx < 0 or bx >= ngrid or by < 0 or by >= ngrid:
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

    
side = 1
rframe = Frame(root)
start = Button(rframe,text="Start",command=gamestart)
exit  = Button(rframe,text="Exit",command=gameexit)
canvas = Canvas(root,width=winsize,height=winsize)

start.pack(side=BOTTOM)
exit.pack(side=BOTTOM)
canvas.pack(side=LEFT)
rframe.pack(side=LEFT)
initArray()
draw()

canvas.bind("<Button-1>",mouseclick)

root.mainloop()
