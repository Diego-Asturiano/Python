import time
from turtle import Screen, Turtle
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()

screen.listen() # Metodo para mover a la tortuga
screen.onkeypress(player.go_up, key= "Up")
screen.onkeypress(player.go_down, key= "Down")

game_is_on = True
# Todo dentro de este bucle while se va a hacer cada 0.1 segundos
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    # Detecta choque con carro
    for car in cars.all_cars:
        if player.distance(car) < 25:
            level.game_over()
            game_is_on = False
    # Avanza al siguiente nivel
        elif player.ycor() == 280:
            player.goto(STARTING_POSITION)
            level.next_level()
            cars.STARTING_MOVE_DISTANCE += cars.MOVE_INCREMENT

screen.exitonclick()

