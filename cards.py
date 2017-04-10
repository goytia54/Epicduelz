def init_cards(p_list):
	for i in xrange(len(p_list)):
		p_index = []
		                        c_array = [0,1,2,3]
					                        max_n = 3 #max players -1
								                        for j in xrange(int(num_players)):
											                                r_index = random.randint(0,max_n) #picking the random index
															                                p_index.append(c_array[r_index]) # append the random ID to select players
																			                                temp_var = c_array[max_n] #set temp var
																							                                c_array[max_n] = c_array[r_index] #take the selected value out
																											                                c_array[r_index] =  temp_var #set the selected value as the last element of the array
																															                                max_n-=1 #turn down the list size to make sure no number is picked twice

		file_name = p_list[i].name +'.txt'
		c_file =  open('characters/{0}'.format(file_name),'rb')
		for j, line in enumerate(c_file):
			if j >= 6:
									
