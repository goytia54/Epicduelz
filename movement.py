#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:42:46 2016

@author: Michael
"""

def move_character(max_spaces,board_dim,player,playing_board):
    #3 is 24 options
    #2 is 12 options
    #4 is 40 options
    #5 is 60 possiblites
    possible_moves = []
    for i in range(player.pos[0]-max_spaces,player.pos[0]+max_spaces+1):
        for j in range(player.pos[1]-max_spaces,player.pos[1]+max_spaces+1):
            if abs(player.pos[0]-i) + abs(player.pos[1]-j) <= max_spaces and i >= 0 and j >= 0 and i < board_dim and j < board_dim:
                    possible_moves.append([i,j])
    catch=1
    while catch != 0:
    	try:
		x,y = raw_input('where do you wish to move? (i.e. 10, for x=1,y=0): ')
		fail = int(x),int(y)
		dec = raw_input('Are you sure you want to move to '+str(x)+' '+str(y)+' ? (y or n): ')
		mv_allowed = move_allowed(x,y,possible_moves)
		if dec == 'y' and mv_allowed == True:
			catch = 0
			playing_board[int(x)][int(y)] = player.player_ID
			playing_board[player.pos[0]][player.pos[1]] = 0 
			player.pos = [int(x),int(y)]
		else:
			print 'Movement is not allowed'
	except ValueError:
		print 'Please enter in valid cooridantes'

    return player,playing_board

def move_allowed(x,y,possible_moves):
	for i in xrange(len(possible_moves)):
		if possible_moves[i][0] == int(x) and possible_moves[i][1] == int(y):
			return True
	return False
