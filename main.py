# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from board import *
from classes import *
from movement import *
from init_game import *
from init_character import *
from cards import *

def main():
    turns = 0
    board_dim = 7
    playing_board = board() #initializes the game board
    p_index = init_game() # number of players    
    p_list = init_character(p_index)
    init_cards(p_list)
    place_character(p_list,playing_board)
    draw_board(playing_board,board_dim)
    i = 0
    game = 1
    while game != 0:
	if i >= len(p_list):
		i = 0 
    	max_spaces = dice_roll(p_list[i])
    	p_list[i],playing_board = move_character(max_spaces,board_dim,p_list[i],playing_board)
    	draw_board(playing_board,board_dim)
        i+=1		

main()
