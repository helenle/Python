# Huyen Le

# template for "Stopwatch: The Game"

import simplegui

# define global variables
int_timer = 0
success_stop = 0
total_stop = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
	A = 0
	B = 0
	C = 0
    if (t < 10):		
		D = t % 10
	elif (10 < t < 600):
		B = t // 100
		C = (t % 100) // 10
		D = t % 10
	else:
		A = t // 600
		B = (t % 600) / 100
		C = ( t % 600) / 10
		D = t % 10
	str_timer = str(A) + ':' + str(B) + str(C) + '.' + str(D)
	return str_timer
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
        
def reset():
    global int_timer
    int_timer = 0
       
# define event handler for timer with 0.1 sec interval
def tick():
    global int_timer
    int_timer += 1
       
timer = simplegui.create_timer(100, tick)

# define draw handler
def draw(canvas):
    global counter
    winning_str = str(success_stop) + '/' + str(total_stop)
    canvas.draw_text(str(winning_str), [150, 30], 30, "Green")
    canvas.draw_text(format(int_timer), [60, 100], 35, "White")

# create frame
frame = simplegui.create_frame("Counter with buttons", 200, 150)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()

