# Huyen Le
# Counter with buttons

###################################################

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
#    print counter
    counter += 1
    
# Event handlers for buttons    
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global counter
    counter = 0
        
def draw(canvas):
    global counter
    canvas.draw_text(str(counter), [20, 20], 20, "White")
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000, tick)

frame.start()

# Start timer
#timer.start()
