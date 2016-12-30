#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:15:23 2016

@author: Michael
"""
import random
import os
from prompt import *


# initialize the playing board
def board():
    playing_board = [[0 for y in xrange(7)] for x in range(7)] #board grid
    return playing_board
    
# roll the dice
def dice_roll(player):
    roll = random.randint(1,6)
    if roll == 1: # one character can move 3 places
        max_spaces = 3
        roll_string ='player {0}, {1}, you rolled a 3'.format(player.ID,player.name)
    elif roll == 2: # 3 all
        max_spaces = 3
        roll_string ='player {0}, {1}, you rolled a 3 ALL'.format(player.ID,player.name)
    elif roll == 3: # 4
        max_spaces = 4
        roll_string ='player {0}, {1}, you rolled a 4'.format(player.ID,player.name)
    elif roll == 4: # 5
        max_spaces = 5
        roll_string ='player {0}, {1}, you rolled a 5'.format(player.ID,player.name)
    elif roll == 5: # 2 all
        max_spaces = 2
        roll_string ='player {0}, {1}, you rolled a 2 ALL'.format(player.ID,player.name)
    else:          # 4 all
        max_spaces = 4
        roll_string ='player {0}, {1}, you rolled a 4 ALL'.format(player.ID,player.name)
    print roll_string
    return max_spaces

# place each character on the board using the p_list object that contains all player info
def place_character(p_list,playing_board):
    for i in range(len(p_list)):
    	playing_board[p_list[i].pos[0]][p_list[i].pos[1]] = p_list[i].ID
    	print '{0} PLACED ON POSTION {1},{2}'.format(p_list[i].name,p_list[i].pos[0],p_list[i].pos[1])

# draws the game board in descending values of y
#  7
#  6
#  5
#  ..

5def draw_board(playing_board,board_dim):
    os.system('cls' if os.name == 'nt' else 'clear')
    game_prompt()    
    board_str=''
    bd_loop = board_dim-1
    board_str+='\n  '+board_dim*'---'+'\n'
    for i in xrange(board_dim):
    	board_str += str(bd_loop-i)+'|'
        for j in xrange(board_dim):
		board_str+= ' ' + str(playing_board[j][bd_loop-i])+ ' ' 
	board_str+= '\n'
    board_str+='  '+board_dim*'---'+'\n  '
    for i in xrange(board_dim):
            board_str+=' '+str(i)+' '
    print board_str   
 
        


          
    
