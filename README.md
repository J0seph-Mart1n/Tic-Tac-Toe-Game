# Tic-Tac-Toe-Game
I made a Tic Tac Toe Game using Python 

Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

Some suggested tools before you get started:
To take input from a user:

player1 = input("Please pick a marker 'X' or 'O'")
Note that input() takes in a string. If you need an integer value, use

position = int(input('Please enter a number'))

To clear the screen between moves:

from IPython.display import clear_output
clear_output()
Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:

print('\n'*100)
This scrolls the previous board up out of view. Now on to the program!

Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game.


I was able to build this game from the course The Complete Python Bootcamp From Zero to Hero in Python.
Jose Portilla the author of the course taught me to build this game.
I would recommend enrolling in the course.
It is available in Udemy.
