#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:15:23 2016

@author: Michael
"""
import random
import os
from prompt import *

def board():
    playing_board = [[0 for y in xrange(7)] for x in range(7)] #board grid
    return playing_board
    
def dice_roll():
    roll = random.randint(1,6)
    
    if roll == 1: # one character can move 3 places
        max_spaces = 3
        roll_string ='your rolled a 3'
    elif roll == 2: # 3 all
        max_spaces = 3
        roll_string ='your rolled a 3 ALL'
    elif roll == 3: # 4
        max_spaces = 4
        roll_string ='your rolled a 4'
    elif roll == 4: # 5
        max_spaces = 5
        roll_string ='your rolled a 5'
    elif roll == 5: # 2 all
        max_spaces = 2
        roll_string ='your rolled a 2 ALL'
    else:          # 4 all
        max_spaces = 4
        roll_string ='your rolled a 4 ALL'
    print roll_string
    return max_spaces
      
def place_character(pos,playing_board,ID):
    playing_board[pos[0]][pos[1]] = ID
    print 'PLAYER {0} PLACED ON POSTION {1},{2}'.format(ID,pos[0],pos[1])
    
def draw_board(playing_board,board_dim):
    os.system('cls' if os.name == 'nt' else 'clear')
    game_prompt()    
    board_str=''
    bd_loop = board_dim-1
    board_str+='\n  '+board_dim*'---'+'\n'
    for i in xrange(board_dim):
    	board_str += str(bd_loop-i)+'|'
        for j in xrange(board_dim): 
		board_str+= ' '+str(playing_board[bd_loop-i][j])+ ' ' 
	board_str+= '\n'
    board_str+='  '+board_dim*'---'+'\n  '
    for i in xrange(board_dim):
            board_str+=' '+str(i)+' '
    print board_str   
 
        


          
    
