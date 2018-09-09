# SA1 solution by Mehdi Oulmakki
# Draws the flag of niger using aluLib

from aluLib import *

window_width = 1500
window_height = 900


def main():
    rectangle_height = window_height / 3

    # draw top rectangle
    set_fill_color(1, 0.5, 0)
    draw_rectangle(0, 0, window_width, rectangle_height)

    # draw center circle
    draw_ellipse(window_width / 2 , window_height / 2, 125, 125)

    # draw bottom rectangle
    set_fill_color(0, 1, 0)
    draw_rectangle(0, 2 * rectangle_height, window_width, rectangle_height)


start_graphics(main, width=window_width, height=window_height)
