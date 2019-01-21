#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:21:59 2019

@author: thieblin
"""

from graphe import Graphe

def parcours_en_profondeur(graphe,sommet):
    g.sommets["a"].visiter()
    g.arcs["ab"].choisir()
    g.sommets["b"].visiter()
    g.plot()
    g.arcs["bd"].choisir()
    g.sommets["d"].visiter()
    g.plot()
    
def parcours_en_largeur(graphe,sommet):
    g.sommets["a"].visiter()
    g.arcs["ab"].choisir()
    g.sommets["b"].visiter()
    g.plot()
    g.arcs["ae"].choisir()
    g.sommets["e"].visiter()
    g.plot()




if __name__=="__main__":
    g = Graphe()
    g.graph_from_file("../maps/graphe4.txt")
    g.plot()
    #parcours_en_largeur(g,"a")
    #g.reset()
    #parcours_en_profondeur(g,"a")

    
