from splashkit import *

# Create diamond shaped quads
q1 = quad_from(400, 200, 300, 300, 300, 0, 200, 200)
q2 = quad_from(400, 210, 310, 300, 600, 300, 400, 390)
q3 = quad_from(200, 400, 300, 300, 300, 600, 400, 400)
q4 = quad_from(200, 390, 290, 300, 0, 300, 200, 210)

# Create two Windows
window1 = open_window("Filled Diamond On Window 1", 600, 600)
window2 = open_window("Filled Diamond On Window 2", 600, 600)

# Move windows to see both side by side
move_window_to(window1, 0, 0)
move_window_to(window2, window_width(window1), 0)

clear_screen(color_white())

# Draw the first and second quad on first window
fill_quad_on_window(window1, color_black(), q1)
fill_quad_on_window(window1, color_green(), q2)

# Draw the third and fourth quad on second window
fill_quad_on_window(window2, color_red(), q3)
fill_quad_on_window(window2, color_blue(), q4)

refresh_screen()
delay(5000)
close_all_windows()