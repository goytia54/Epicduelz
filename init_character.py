from classes import *
import os

def init_character(p_index):
	os.chdir('characters')
	character_array = ['darth_maul.txt','obi_wan.txt','luke.txt','darth_vader.txt']
	p_list = []
	for l in xrange(len(p_index)):
		file_string = character_array[p_index[l]]
		char_file =  open(file_string,'rb')
		for i, line in enumerate(char_file):
			if i ==1:
		       		in_line = line.split()
				name = in_line[0]
			elif i == 2:
				in_line = line.split()
				life = int(line[0])
			elif i == 3:
				in_line = line.split()
				pos = [int(in_line[0]),int(in_line[1])]
			elif i == 4:
				in_line = line.split()
				at =  int(in_line[0])
		char_file.close()
		s = Player(pos,4,at,life,l+1,name)
		p_list.append(s)
	os.chdir('..')
	return p_list

