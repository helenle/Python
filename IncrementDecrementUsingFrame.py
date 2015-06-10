# GUI with buttons to manipulate global variable count

import simplegui

count = 0

# Define event handlers for four buttons
    
# Reset global count to zero.
def reset():
    global count
    count = 0
    
# Increment global count.
def increment():
    global count
    count += 1
    
# Decrement global count.
def decrement():
    global count
    count -= 1
    
# Print global count.
def print_count():
    global count
    return count
    
#draw on canvas
def draw(canvas):
    global count
    canvas.draw_text(str(count), [50,50], 24, "White")
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Counter", 300, 200)
frame.add_button("Reset", reset, 100)
frame.add_button("Increment", increment, 100)
frame.add_button("Decrement", decrement, 100)
frame.add_button("Print", print_count, 100)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
''' This test print to the console.
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()
'''
####################################################
# Expected output from test

#1
#2
#-2
