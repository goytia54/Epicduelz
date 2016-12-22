from prompt import *
import os
import random

def init_game():
	catch =1
	os.system('cls' if os.name == 'nt' else 'clear')
	game_prompt()
	while catch != 0:
		try:
			num_players = raw_input('How many players will be playing the game(2-4): ')
			character_assign(num_players)
			catch = 0
		except ValueError:
			print 'Please indicate the correct amount players'
		except IndexError:
			print 'Please indicate the correct amount players'


def character_assign(num_players):
	p_index = []
	character_array = ['darth_maul.txt','obi_want.txt','luke.txt.','darth_vader.txt']
	c_array = [0,1,2,3,4]
	max_n = 4
        for j in xrange(int(num_players)):
		print j,'begin',c_array
		r_index = random.randint(0,max_n) #picking the random index
		p_index.append(c_array[r_index])
		temp_var = c_array[max_n]
		c_array[max_n] = c_array[r_index]
		c_array[r_index] =  temp_var
		print j,'end',c_array
		print p_index
		max_n-=1

		
	
			
