# Your name goes here

from aluLib import *
from math import sqrt, pow

window_width = 1000
window_height = 600

# Note that functions are expected to be lowercase, so don't be tempted to capitalize
def benin():
    enable_fill()
    #Vertical green rectangle
    set_fill_color(0, 0.53, 0.32)
    draw_rectangle(0, 0, window_width//3, window_height)
    #Horizontal yellow rectangle
    set_fill_color(0.98, 0.82, 0.08)
    draw_rectangle(window_width//3, 0, window_width - window_width//3, window_height//2)
    #Horizontal red rectangle
    set_fill_color(0.9, 0.06, 0.17)
    draw_rectangle(window_width//3, window_height//2, window_width - window_width//3, window_height//2)




def niger():
    enable_fill()
    #First horizontal orange rectangle
    set_fill_color(.87, .32, .02)
    draw_rectangle(0, 0, window_width, window_height // 3)
    #White horizontal rectangle with orange circle in its middle
    set_fill_color(.87, .32, .02)
    draw_circle(window_width//2, window_height//2, window_height//6 - 10)
    #Green rectangle
    set_fill_color(.05, .7, .16)
    draw_rectangle(0, 2 * window_height//3, window_width, window_height // 3)

def guinea():
    enable_fill()
    # Vertical red rectangle
    set_fill_color(.8, .06, .15)
    draw_rectangle(0, 0, window_width // 3, window_height)
    # Vertical yellow rectangle
    set_fill_color(.98, .82, .08)
    draw_rectangle(window_width // 3, 0, window_width // 3, window_height)
    # Vertical green rectangle
    set_fill_color(0, .58, .37)
    draw_rectangle(2 * window_width // 3, 0, window_width // 3, window_height)

def morocco():
    enable_fill()
    disable_stroke()
    #The red background
    set_fill_color(.75, .15, .17)
    draw_rectangle(0, 0, window_width, window_height)

    #The green star in the center
    disable_fill()
    enable_stroke()
    set_stroke_color(0, .38, .2)
    set_stroke_width(15)

    star_width = window_width/5
    #space between the star and the left or right edge
    side_margin = 2 * window_width/5
    #space between the star and the top or bottom of the flag
    vertical_margin = window_height/3
    #height of the tip of the star
    star_tip_height = sqrt(pow(star_width/3, 2) - pow(star_width/6, 2))

    draw_polygon([[side_margin, vertical_margin + star_tip_height], \
                  [side_margin + star_width, vertical_margin + star_tip_height], \
                  [side_margin + star_width / 6, vertical_margin + star_width], \
                  [side_margin + star_width / 2, vertical_margin],
                  [side_margin + 5 / 6 * star_width, vertical_margin + star_width]])


start_graphics(morocco, width=window_width, height=window_height)