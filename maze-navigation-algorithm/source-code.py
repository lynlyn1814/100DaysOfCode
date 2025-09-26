# Please read the information.md file in the same folder as this before reading the source code to prevent confusion

# Reeborg function to set how long the millisecond delay is between each step. This makes it as fast as possible.
think(0)

# Declaring a global variable that will be used to identify if you're stuck in an edge-case loop
right_turns = 0

# Reeborg only has turn_left(), so I made it easier to turn right by creating my own function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# This kicks into action whenever the right_turns variable is equal to 4, and will tackle EVERY edge case for this map
def loop_fallback():
    global right_turns
    if is_facing_north(): # Fixes 2/3 edge cases
        move()
        right_turns = 0
    else:                 # Fixes the remaining edge case
        turn_left()
        turn_left()
        move()
        right_turns = 0
        
# The main pathfinding algorithm
def pathfind():
    global right_turns # "Importing" the global right_turns variable
    if right_turns == 4: # Activates the loop_fallback() function whenever the robot is stuck in a loop
        loop_fallback()
    elif right_is_clear(): # The algorithm is based off of a rule for solving mazes where as long as you stick to the right at all times you'll find the way out
        turn_right()
        move()
        right_turns = right_turns + 1
    elif front_is_clear():
        move()
        right_turns = 0
    else:
        turn_left()
        right_turns = 0

while not at_goal(): # This is the while loop that runs the pathfinding algorithm until the end is reached
    pathfind()
