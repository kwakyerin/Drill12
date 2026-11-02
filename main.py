from pico2d import *
from boy import Boy
from grass import Grass
from ball import Ball
from grass_01 import GrassGG


import game_world


# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)
            direction = boy.consume_shot()
            if direction is not None:
                #공 그린 위치
                game_world.add_object(Ball(
                    boy.x + direction * 40, boy.y, direction), 1)



def reset_world():
    global boy

    boy = Boy()
    game_world.add_object(boy,0)

    grass = Grass()
    game_world.add_object(grass,1)

    grass_01=GrassGG()
    game_world.add_object(grass_01,0)



def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True

open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
