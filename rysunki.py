import turtle

lista = [6,0,7,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,4,1,4,1,2,1,2,1,4,1,4,1,2,1,2,1,4,1,4,1,2,1,2,1,4,1,4,1,2,1,2,1,4,1,4,1,2,1,2,1,4,1,4,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,8,1,1,1,4,1,1,4,1,1,1,9,2,1,2,6,1,1,1,1,1,1,7,77,1,4,1,8, 10,9,8,1,4,1,4,1,9,8,1,4,1,1,4,1,1,4,1,9,1,4,6,1,1,1,1,1,1,1,1,7,4, 77, 1,4,1,8, 10,9,8,1,4,1,4,1,9,8,1,4,1,1,4,1,1,4,1,9] #9
 
zolw = turtle.Turtle()
zolw.fillcolor('green')
zolw.color('green')
zolw.pensize(3)

for element in lista:
    if element == 1:
        zolw.forward(50)
    elif element == 2:
        zolw.left(90)
    elif element == 3:
        zolw.left(45)
    elif element == 4:
        zolw.right(90)
    elif element == 5:
        zolw.right(45)
    elif element == 6:
        zolw.penup()
    elif element == 7:
        zolw.pendown()
    elif element == 8:
        zolw.begin_fill()
    elif element == 9:
        zolw.end_fill()
    elif element == 10:
        zolw.circle(50)
    elif element == 0:
        zolw.setpos(-300, -300)

input()
    
        
