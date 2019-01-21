#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:21:59 2019

@author: thieblin
"""

from graphe import Graphe
from arc import Arc

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

adjacent = {}
num = {}

def base(arc):
    adjacent[arc.cible] = arc.cible
    num[arc.cible] = 0
    num[arc.source] = 1

def find(arc):
    if adjacent[arc.cible] != arc.cible:
        adjacent[arc.cible] = find(adjacent[arc.cible])
        return False
    else:
        return True
        return adjacent[arc.cible]

def union(arc):
    base1 = arc.cible
    base2 = arc.source
    if base1 != base2:
        if num[base1] > num[base2]:
            adjacent[base2] = base1
        else:
            adjacent[base1] = base2
        if num[base1] == num[base2]: num[base2] += 1

def kruskal(graphe):
    liste = []
    arc = graphe.arcs.values()
    arc = sorted(arc, key=lambda arc: arc.value)
    for i in arc:
        base(i)
        if find(i):
            union(i)
            liste.append(i)
    return liste

if __name__=="__main__":
    g = Graphe()
    g.graph_from_file("graphe1.txt")
    print(kruskal(g))
    g.plot()
    #parcours_en_largeur(g,"a")
    #g.reset()
    #parcours_en_profondeur(g,"a")

    
