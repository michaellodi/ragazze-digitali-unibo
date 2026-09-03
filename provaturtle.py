import turtle
import random

turtle.speed(1)
turtle.pensize(5)

# I colori vengono usati a turno, uno diverso per ogni segmento
colori = ["red", "orange", "yellow", "lime", "cyan", "blue", "violet"]

lunghezza = 5

for segmento in range(80):
    turtle.pencolor(random.choice(colori))
    turtle.forward(lunghezza)
    turtle.left(90)
    lunghezza = lunghezza + 7

turtle.done()