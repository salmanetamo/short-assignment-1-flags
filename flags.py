# Your name goes here

from aluLib import *

window_width = 1000
window_height = 600

# Note that functions are expected to be lowercase, so don't be tempted to capitalize
def benin():
    enable_fill()
    #Vertical green rectangle
    set_fill_color(0, 1, 0)
    draw_rectangle(0, 0, window_width//3, window_height)
    #Horizontal yellow rectangle
    set_fill_color(1, 1, 0)
    draw_rectangle(window_width//3, 0, window_width - window_width//3, window_height//2)
    #Horizontal red rectangle
    set_fill_color(1, 0, 0)
    draw_rectangle(window_width//3, window_height//2, window_width - window_width//3, window_height//2)




def niger():
    enable_fill()
    #First horizontal orange rectangle
    set_fill_color(1, .5, 0)
    draw_rectangle(0, 0, window_width, window_height // 3)
    #White horizontal rectangle with orange circle in its middle
    set_fill_color(1, .5, 0)
    draw_circle(window_width//2, window_height//2, window_height//6 - 10)
    #Green rectangle
    set_fill_color(0, 1, 0)
    draw_rectangle(0, 2 * window_height//3, window_width, window_height // 3)

def guinea():
#     print('guinea')


start_graphics(niger, width=window_width, height=window_height)