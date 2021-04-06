# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:41:38 2021

@author: ErikB
"""

#FEMALE_NAMES = open("./names/female/namelist.txt", 'r').readlines()

import random
import string

def populate_name_list(txt_dir):
    '''
    Parameters
    ----------
    txtdir : directory where name_list is located

    Returns
    -------
    Tuple
        List of names from provided name list.
    '''
    result = sorted(set(word
    for line in open(txt_dir)
    for word in line.split()))
    return tuple(result)

FEMALE_NAMES = populate_name_list('./names/female/namelist.txt')
MALE_NAMES   = populate_name_list('./names/male/namelist.txt')
LAST_NAMES   = populate_name_list('./names/last/namelist.txt')

# def random_nameOriginal():
#     '''
#     Original random_name that asks the user for input to determine sex.    
#     '''
#     import random
#     full_name = ""
#     def name_compilation(x):
#         r_name = random.choice(x)
#         l_name = random.choice(LAST_NAMES)
#         full_name = r_name + ' ' + l_name
#         return full_name.title()     
#     while full_name == "":
#         char_sex = input('What Sex is your Character, Male, Female, or Either: ')
#         if char_sex.lower() == 'male':
#             print("Your Character's name is: ", name_compilation(MALE_NAMES))
#             break
#         elif char_sex.lower() == 'female':
#             print("Your Character's name is: ", name_compilation(FEMALE_NAMES))
#             break    
#         elif char_sex.lower() == 'either':
#             print("Your Character's name is: ", name_compilation(FEMALE_NAMES + MALE_NAMES))
#             break     
#         else:
#             print("Hmm, seems like you typed some bullshit in there, try again and don't fuck up...")   

def random_name(x, last_name):
    
    full_name = ""
   
    while full_name == "":
        char_sex = x
        if char_sex.lower() == 'male':
            return name_compilation(MALE_NAMES, last_name)
        elif char_sex.lower() == 'female':
            return name_compilation(FEMALE_NAMES, last_name)
            break    
        else:
            return name_compilation(FEMALE_NAMES + MALE_NAMES, last_name)
            break     
        
def name_compilation(x, last_name=None):
    ''' 
    Parameters
    ----------
    x : tuple
        Designates which name list to use based on selected gender.
    last_name : str, optional
        If no last name is provided one will be selected at random.
    Returns
    -------
    String
        Full name, formatted by title method
    '''
    if last_name == None:
        last_name = random.choice(LAST_NAMES)
    first_name = random.choice(x)
    full_name = first_name + ' ' + last_name
    return full_name.title()     


def family_unit():
    
    x = ''
    fam_size = random.randint(3,10)
    family = []
    x_determine = 0
    last_name = random.choice(LAST_NAMES) 
    
    for person in range(fam_size):
        x_determine = random.randint(1,3)
        if x_determine == 1:
            x = 'male'
        elif x_determine == 2:
            x = 'female'
        else:
            x = 'either'
        family.append(random_name(x, last_name))
    return family 

balancer = 0

def family_composition():
    
    gay_chance = random.randint(0,100)
    if gay_chance > 100:
        return family_sort(0)
    else:
        return family_sort(1)
    


def family_sort(distrib_val):
    family = family_unit()
    #family = random.shuffle(family)
    family_dict = {'dad':[],'mom':[],'children':[]}
    global balancer 
    
    
    while balancer % 2 == 0 and distrib_val == 1:
        for member in family:
            if member.upper().split()[0] in MALE_NAMES:
                if len(family_dict['dad']) < 2:
                    family_dict['dad'].append(member)
                else:
                    family_dict['children'].append(member)
            else:
                family_dict['children'].append(member)
        balancer += 1
        return family_dict
    while balancer % 2 != 0 and distrib_val == 1:
        for member in family:
            if member.upper().split()[0] in FEMALE_NAMES:
                if len(family_dict['mom']) < 2:
                    family_dict['mom'].append(member)
                else:
                    family_dict['children'].append(member)
            else:
                family_dict['children'].append(member)        
        balancer += 1
        return family_dict
    while distrib_val != 1:
        for member in family:
            if member.upper().split()[0] in MALE_NAMES:
                if len(family_dict['dad']) != 1:
                    family_dict['dad'].append(member)
                else:
                    family_dict['children'].append(member)
            else:
                if len(family_dict['mom']) != 1:
                    family_dict['mom'].append(member)
                else:
                    family_dict['children'].append(member)
        return family_dict
    
    
    # for member in family:
    #     if member.upper().split()[0] in MALE_NAMES:
    #         if len(family_dict['dad']) == 1 and distrib_val == 1 and balancer % 2 == 0 and len(family_dict['mom']) == 0:
    #             if len(family_dict['children']) == 0:
    #                 family_dict['children'].append(member)
    #             elif family_dict['dad'] < 2:
    #                     family_dict['dad'].append(member)
    #             else:
    #                 family_dict['children'].append(member)
    #             balancer += 1
    #         else:
    #             if len(family_dict['dad']) == 0:
    #                 family_dict['dad'].append(member)
    #             elif member == family[-1] and len('dad') + len('mom') != 2:
    #                 family_dict['dad'].append(member)
    #             else:
    #                 family_dict['children'].append(member)
    #     elif member.upper().split()[0] in FEMALE_NAMES:
    #         if len(family_dict['mom']) == 1 and distrib_val == 1 and balancer % 2 != 0 and len(family_dict['dad']) == 0:
    #             if len(family_dict['children']) == 0:
    #                 family_dict['children'].append(member)
    #             elif family_dict['mom'] < 2:
    #                 family_dict['mom'].append(member)
    #             else:
    #                 family_dict['children'].append(member)
    #             balancer += 1
    #                 #distrib_val -= 1
    #         else:
    #             if len(family_dict['mom']) == 0:
    #                 family_dict['mom'].append(member)
    #             elif member == family[-1] and len('dad') + len('mom') != 2:
    #                 family_dict['mom'].append(member)
    #             else:
    #                 family_dict['children'].append(member)               
    

    
# def fam_distributor(distrib_val):
    
#     family = family_unit()
#     dad = []
#     mom = []
#     kids = []
    
#     for family_member in family:
#         if family_member.upper().split()[0] in MALE_NAMES:
#             if len(dad) > distrib_val or len(mom) > 1:
#                 kids.append(family_member)
#             else:
#                 dad.append(family_member)
#         else:
#             if len(mom) > distrib_val or len(dad) > 1:
#                 kids.append(family_member)
#             else:
#                 mom.append(family_member)
   
#     family_group = {'dad':dad, 'mom':mom, 'kids':kids}
#     if len(family_group['dad']) == 0:
#         del family_group['dad']
#     if len(family_group['mom']) == 0:
#         del family_group['mom']
#     #if len(family_group['kids']) == 0:
#     #    del family_group['kids']
#     return family_group

def many_families(x):
    num_fam = range(x)
    community = []
    counter = 0
    
    for i in num_fam:
        counter += 1
        #community.append(str("family"+str(counter)+":"))
        community.append(family_composition())
        print (balancer)
    return community
    

town_population = 30
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

def descriptive_town():
    roster = many_families(town_population)
    
    for family in roster:
        print("__________")
        print(family)
        print("__________")

    
