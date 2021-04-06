# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 23:57:04 2021

@author: ErikB
"""

import towngen_syntax_rewrite.py
    
town_population = 100
pop_co = round(town_population / 98)
town = {"Mayor"             : 1,
        "Mayor's Aid"       : 1,
        "Council Members"   : round(1.2 * pop_co),
        "Blacksmiths"       : round(1.2 * pop_co),
        "Tailors"           : round(1.3 * pop_co),
        "Doctors"           : round(1.5 * pop_co),
        "Guards"            : round(1.7 * pop_co),
        "Whores"            : round(2 * pop_co),
        "Farmers"           : round(3 * pop_co),
        "Peddlers"          : round(2 * pop_co)
        }



def commoner_calc(town, town_population):
    
    total = sum(list(town.values()))
    commoners = town_population - total
    return commoners
    
town["Commoners"] = commoner_calc(town, town_population)

assign_prof = []
town_names = many_families(town_population())

for profession in town.values():
    assign_prof.append()