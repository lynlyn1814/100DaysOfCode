# Context
This is a Python algorithm for [**Reeborg's World**](reeborg.ca) that utilises The Right Hand Rule for solving 2D mazes.
It works by always trying to turn right, if it can't then it will move forwards, and if it can't do that then it moves to the left.

There are exactly three different edge cases where you'll be stuck in an endless loop.
While the course I got this exercise from recommended not to worry about the edge cases yet since it's only day 5, I already had an idea in mind.
My approach was to use a global variable to track the amount of right turns, so that if I turn right 4 times in a row then I know I'm in a loop.
Once I detect that, I call a custom function that will fix it depending on which edge case is being experienced.
After doing this, the instructor of the course gave her own solution which was far more elegant, however I think I did okay with what I knew.

# Example
https://github.com/user-attachments/assets/670b271c-0ca4-42fc-b295-837f69a8bd2f
