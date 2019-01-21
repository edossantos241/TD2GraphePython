#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:28:25 2019

@author: thieblin
"""

import math
import matplotlib.pyplot as plt


class Arc:
    def __init__(self,source, cible,value=1):
        self.source=source
        self.cible=cible
        self.value=value
        self.choisi=False
    
    def choisir(self):
        self.choisi=True
    
    def estChoisi(self):
        return self.choisi
    
    def inverse(self):
        return Arc(self.cible,self.source,value=self.value)
        
    def euclidean_value(self):
        return math.sqrt((self.source.lat-self.cible.lat)**2+(self.source.long-self.cible.long)**2)
    
    def middle(self):
        out= ((self.source.long+self.cible.long)*0.5,(self.source.lat+self.cible.lat)*0.5)
        return out
    
    def marker(self):
        diff_x=self.cible.long - self.source.long
        diff_y=self.cible.lat - self.source.lat
        if (abs(diff_x) < abs(diff_y)):
            if diff_y<0:
                marker='v'
            else:
                marker='^'
        else:
             if diff_x <0:
                marker='<'
             else:
                marker='>'
           
        return marker
    
    def reset(self):
        self.choisi = False