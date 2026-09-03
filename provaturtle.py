import turtle

turtle.speed(0)
turtle.pensize(3)

# I colori vengono usati a turno, uno diverso per ogni segmento
colori = ["red", "orange", "yellow", "lime", "cyan", "blue", "violet"]

lunghezza = 5

for segmento in range(80):
    turtle.pencolor(colori[segmento % len(colori)])
    turtle.forward(lunghezza)
    turtle.left(90)
    lunghezza += 4

turtle.hideturtle()
turtle.done()
