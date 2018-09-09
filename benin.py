# SA1 solution by Mehdi Oulmakki
# Draws the flag of benin using aluLib

from aluLib import *

window_width = 1500
window_height = 900


def main():
    vertical_rect_width = window_width / 3
    horizontal_rect_width = vertical_rect_width * 2
    horizontal_rect_height = window_height / 2

    # draw left most rectangle in green
    set_fill_color(0, 0.8, 0)
    draw_rectangle(0, 0, vertical_rect_width, window_height)

    # draw top rectangle in yellow
    set_fill_color(1, 1, 0)
    draw_rectangle(vertical_rect_width, 0, horizontal_rect_width, horizontal_rect_height)

    # draw bottom most rectangle in red
    set_fill_color(1, 0, 0)
    draw_rectangle(vertical_rect_width, horizontal_rect_height, horizontal_rect_width, horizontal_rect_height)


start_graphics(main, width=window_width, height=window_height)