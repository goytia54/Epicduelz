from prompt import *
import os
import random
import cards

def init_game():
	catch =1
	os.system('cls' if os.name == 'nt' else 'clear')
	game_prompt()
	while catch != 0:
		try:
			num_players = raw_input('How many players will be playing the game(2-4): ')
			catch = 0
			p_index = []
			c_array = [0,1,2,3]
			max_n = 3 #max players -1
			for j in xrange(int(num_players)):
				r_index = random.randint(0,max_n) #picking the random index
				p_index.append(c_array[r_index]) # append the random ID to select players
				temp_var = c_array[max_n] #set temp var
				c_array[max_n] = c_array[r_index] #take the selected value out
				c_array[r_index] =  temp_var #set the selected value as the last element of the array
				max_n-=1 #turn down the list size to make sure no number is picked twice
		except ValueError:
			print 'Please indicate the correct amount players'
		except IndexError:
			print 'Please indicate the correct amount players'
		except UnboundLocalError:
			print 'Please indicate the correct amount players'
	return p_index		

