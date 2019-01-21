#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:16:54 2019

@author: thieblin
"""
from sommet import Sommet
from arc import Arc
import matplotlib.pyplot as plt


class Graphe:
    def __init__(self):
        self.sommets={}
        self.arcs={}
        self.nb_sommets=0
        self.nb_arcs=0
        self.oriente=False
        
    def graph_from_file(self,file_name):
        file = open(file_name, "r")
        first_line=[int(x) for x in file.readline().split()]
        self.nb_sommets=first_line[0]
        self.nb_arcs=first_line[1]
        self.oriente=(first_line[2]==1)
        
        # ajout de tous les sommets
        for i in range(self.nb_sommets):
            line=[a for a in file.readline().split()]
            sommet_cur=Sommet(line[0],lat=float(line[1]),long=float(line[2]))
            self.sommets[line[0]]=sommet_cur
            
        # ajout de tous les arcs
        for i in range(self.nb_arcs):
            line=[a for a in file.readline().split()]
            if len(line)==0:
                print(i)
            else:
                s_source = self.sommets[line[0]]
                s_cible = self.sommets[line[1]]
                arc_cur=Arc(s_source,s_cible,value=float(line[2]))
                self.arcs['%s%s' % (s_source.name,s_cible.name)] = arc_cur
                # si le graphe n'est pas orienté, on ajoute l'inverse de chaque arc
                if not self.oriente:
                    self.arcs['%s%s' % (s_cible.name,s_source.name)] = arc_cur.inverse()
                
        
        file.close()

    def reset(self):
        for sommet in self.sommets.values():
            sommet.reset()
        for arc in self.arcs.values():
            arc.reset()

        
    def plot(self):
        for arc in self.arcs.values():
            if(arc.estChoisi()):
               colour = 'r'
            else:
               colour = 'lightgrey'
            plt.plot([arc.source.long,arc.cible.long],[arc.source.lat,arc.cible.lat],'-',color=colour)
            if(self.oriente):
                plt.plot(arc.middle()[0],arc.middle()[1],arc.marker(),color=colour)
            plt.annotate('%s' % arc.value, xy=arc.middle(), textcoords='data')
        x=[]
        x_visited=[]
        y=[]
        y_visited=[]
        for sommet in self.sommets.values():
            if(sommet.estVisite()):
                x_visited.append(sommet.long)
                y_visited.append(sommet.lat)
            else:
                x.append(sommet.long)
                y.append(sommet.lat)
            plt.annotate('%s' % sommet.name, xy=(sommet.long,sommet.lat), textcoords='data')
            plt.plot(x_visited,y_visited,'ro',markersize=20)
            plt.plot(x,y,'o',markersize=20,markerfacecolor='lightgrey')
        plt.show()