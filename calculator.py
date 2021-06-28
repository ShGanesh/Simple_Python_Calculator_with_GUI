# A simple Calculator in Python with GUI
import time
from graphics import *  # pip3 import graphics.py

def main():
    workArea = GraphWin('Simple Calculator', 250, 350) # Title and Dimensions
    workArea.setBackground('black')
    calexp = Rectangle(Point(50,10),Point(190,40))
    calexp.setFill("light yellow")
    calexp.draw(workArea)
    arrf = []
    arrt = []
    x = 50
    y = 50
    i = 0
    j = 9
    #loop to create number buttons
    while j>0:
        arrf.append(Point(x, y))
        arrt.append(Point(x+50, y+50))
        btn=Rectangle(Point(x,y),Point(x+50, y+50))
        btn.setFill('white')
        btn.draw(workArea)
        num = Text(Point(x+25,y+25),str(j))
        num.setFace('helvetica')
        num.setStyle('bold italic')
        num.setTextColor("blue")
        num.draw(workArea)
        x = x + 55
        j = j - 1
        i = i + 1
        if (i == 3):       
            x = 50
            y = y + 55
            i = 0
    ops = ['+', '0', '-', '*', '÷', '=']
    j = 0
    #loop to create operator buttons
    while j<len(ops):
        arrf.append(Point(x, y))
        arrt.append(Point(x + 50 ,y + 50))
        btn=Rectangle(Point(x, y), Point(x + 50, y + 50))
        btn.setFill('white')
        btn.draw(workArea)
        num = Text(Point(x + 25, y + 25), str(ops[j]))
        if ops[j] == "0":
            num.setFace('helvetica')
            num.setStyle('bold italic')
            num.setTextColor("blue")
        else:
            num.setFace('helvetica')
            num.setStyle('bold italic')
            num.setSize(22)
            num.setTextColor("red")
        num.draw(workArea)
        x = x + 55
        j = j + 1
        i = i + 1
        if (i == 3):       
            x = 50
            y = y + 55
            i = 0

    # Create Clear button           
    btn=Rectangle(Point(192,10),Point(222,40))
    btn.setFill('green')
    btn.draw(workArea)
    arrf.append(Point(192,10))
    arrt.append(Point(222,40))
    num = Text(Point(192+15,10+15),'C')
    num.setFace('helvetica')#change text style
    num.setStyle('bold italic')
    num.setTextColor("white") #change text color
    num.draw(workArea)
    
    numv=""
    clk=True
    #loop to check the range of coortinates where user clicked
    while clk:
        ch=workArea.getMouse()
        if (ch.x >arrf[0].x  and ch.x <arrt[0].x and ch.y >arrf[0].y  and ch.y<arrt[0].y):
            numv=numv+"9"
        if (ch.x >arrf[1].x  and ch.x <arrt[1].x and ch.y >arrf[1].y  and ch.y<arrt[1].y):
            numv=numv+"8"
        if (ch.x >arrf[2].x  and ch.x <arrt[2].x and ch.y >arrf[2].y  and ch.y<arrt[2].y):
            numv=numv+"7"
        if (ch.x >arrf[3].x  and ch.x <arrt[3].x and ch.y >arrf[3].y  and ch.y<arrt[3].y):
            numv=numv+"6"
        if (ch.x >arrf[4].x  and ch.x <arrt[4].x and ch.y >arrf[4].y  and ch.y<arrt[4].y):
            numv=numv+"5"
        if (ch.x >arrf[5].x  and ch.x <arrt[5].x and ch.y >arrf[5].y  and ch.y<arrt[5].y):
            numv=numv+"4"
        if (ch.x >arrf[6].x  and ch.x <arrt[6].x and ch.y >arrf[6].y  and ch.y<arrt[6].y):
            numv=numv+"3"
        if (ch.x >arrf[7].x  and ch.x <arrt[7].x and ch.y >arrf[7].y  and ch.y<arrt[7].y):
            numv=numv+"2"
        if (ch.x >arrf[8].x  and ch.x <arrt[8].x and ch.y >arrf[8].y  and ch.y<arrt[8].y):
            numv=numv+"1"
        if (ch.x >arrf[9].x  and ch.x <arrt[9].x and ch.y >arrf[9].y  and ch.y<arrt[9].y):
            numv=numv+"+"
        if (ch.x >arrf[10].x  and ch.x <arrt[10].x and ch.y >arrf[10].y  and ch.y<arrt[10].y):
            numv=numv+"0"
        if (ch.x >arrf[11].x  and ch.x <arrt[11].x and ch.y >arrf[11].y  and ch.y<arrt[11].y):
            numv=numv+"-"
        if (ch.x >arrf[12].x  and ch.x <arrt[12].x and ch.y >arrf[12].y  and ch.y<arrt[12].y):
            numv=numv+"*"
        if (ch.x >arrf[13].x  and ch.x <arrt[13].x and ch.y >arrf[13].y  and ch.y<arrt[13].y):
            numv=numv+"/"
        if (ch.x >arrf[14].x  and ch.x <arrt[14].x and ch.y >arrf[14].y  and ch.y<arrt[14].y):
            #Evaluate and display expression
            num.undraw()
            num = Text(Point(150-len(str(numv)),25),str(eval(numv)))
            num.draw(workArea)
            numv=str(eval(numv))
            continue
        if (ch.x >arrf[15].x  and ch.x <arrt[15].x and ch.y >arrf[15].y  and ch.y<arrt[15].y):
            numv="    "
        if (ch.x >249):
            break
        calexp=Rectangle(Point(50,10),Point(190,40))
        calexp.setFill("yellow")
        calexp.draw(workArea)
        num = Text(Point(150-len(str(numv)),25),str(numv))
        num.draw(workArea)
            
main()    

