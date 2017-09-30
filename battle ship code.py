# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:50:17 2017

@author: Wing Ng

This program provides a simple game of battleship where user will guess within a 5 by 5 game board
for one single square where the random battleship may be.  The user has 5 tries, with each turn printed to remind the player.
once a spot is guessed, it will be marked with an X.  If the guess is not in the 5 by 5 board, a statement of "that's not even in the ocean"
will turn up.  

"""

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(4):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
  if turn == 3:
    print ("Game Over")
