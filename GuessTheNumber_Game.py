# template for "Guess the number" mini-project 
# input will come from buttons and an input field 
# all output for the game will be printed in the console

# To play, copy and paste this link to the browser
#http://www.codeskulptor.org/#user21_lvrlXsszrK_1.py

import simplegui
import math
import random

# initialize global variables used in your code 
secret = 0 
lower = 0 
upper = 100
remain_guess_no = 0

# helper function to start and restart the game 
def new_game():
    # calculate the range width and assign a random number to secret variable.
    global upper, lower, secret, remain_guess_no
    secret = random.randrange(lower, upper)
    remain_guess_no = int(math.ceil(math.log(upper - lower + 1, 2)))
    
    print "\nNew game. Range is from 0 to", upper
    print "Number of remain guesses is", remain_guess_no
   
      
# define event handlers for control panel 
def range100():
    # button that changes range to range [0,100) and restarts
    global upper	
    upper = 100    
    new_game()
       
def range1000():
    # button that changes range to range [0,1000) and restarts
    global upper
    upper = 1000  
    new_game()
    
def input_guess(guess):
    # main game logic goes here 
    # get the guess number from input text field
    global remain_guess_no	
    remain_guess_no -= 1
        
    print "\nGuess was", int(guess)
    print "Number of remain guesses is", remain_guess_no
    
    if int(guess) > secret and remain_guess_no > 0:
        print "Lower!"
    elif int(guess) < secret and remain_guess_no > 0:
        print "Higher!"
    elif int(guess) == secret and remain_guess_no >= 0 :
        print "You win!"            
        new_game()
    else: # assert remain_guess_no = 0:
        print "You ran out of guesses. The number was", secret
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements 
button1 = frame.add_button("Range [0, 100)", range100, 150)
button2 = frame.add_button("Range [0, 1000)", range1000, 150) 
text_field = frame.add_input("Enter a guess", input_guess, 150)

# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
