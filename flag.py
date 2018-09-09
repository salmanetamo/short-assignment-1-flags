from aluLib import *


def main():
    set_fill_color(1, 0, 0)
    draw_rectangle(0, 0, 500, 900)

    set_fill_color(1, 1, 0)
    draw_rectangle(500, 0, 500, 900)

    set_fill_color(0, 1, 0)
    draw_rectangle(1000, 0, 500, 900)


start_graphics(main, width=1500, height=900)