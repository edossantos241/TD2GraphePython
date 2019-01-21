#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:17:41 2019

@author: thieblin
"""
import matplotlib.pyplot as plt

class Sommet:
    def __init__(self,name,lat=0.0, long=0.0):
        self.name=name
        self.lat=lat
        self.long=long
        self.visite=False
    
    def visiter(self):
        self.visite=True
    
    def estVisite(self):
        return self.visite
        
    def reset(self):
        self.visite=False