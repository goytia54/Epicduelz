# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from board import *
from classes import *
from movement import *
from init_game import *

def main():
    turns = 0
    board_dim = 7
    playing_board = board() #initializes the game board
    num_players = init_game() # number of players    
    
    
    #place_character(darth_maul.pos,playing_board,darth_maul.player_ID)
    #draw_board(playing_board,board_dim)
    #max_spaces = dice_roll()
    #darth_maul,playing_board = move_character(max_spaces,board_dim,darth_maul,playing_board)
    #draw_board(playing_board,board_dim)
    #turns +=1 

main()
