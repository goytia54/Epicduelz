#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:20:35 2016

@author: Michael
"""

class Player:
    def __init__(self,pos,cih,at,life,ID,name):
            self.pos = pos  #position of te character
            self.cih = cih #cards in hand(cih)
            self.at = at #attack type (at)
            self.life = life # life of characther
            self.ID = ID #ID of player
	    self.name = name #name of player
            
