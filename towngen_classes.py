# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:18:46 2021

@author: ErikB
"""

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

class Settlement(object):
    def __init__(self, n_of_people=100):
        self.population = []
        self.jobs = None
        self.generate_population(n_of_people)
        self.generate_relationships()
        self.print_population_names()
        #this is a list of jobs in town
    
    def get_population(self):
        return self.population
    def print_population_names(self):
        list_len = len(self.population)
        for i in range(list_len):
            print (self.population[i].get_full_name())
            
    
    def set_population(self, list_of_people):
        self.population = list_of_people
    def generate_population(self, n=5):
        #takes in n number of people you want to generate
        new_population = []
        for _ in range(n):
            new_person = Person()
            new_population.append(new_person)
            #generates a new person from Person class
            #new_population.append(person) #this var is placeholder
        self.set_population(new_population)
    def generate_relationships(self):
        temp_list = self.population[:]
        temp_straight = []
        temp_gay = []
        temp_bi = []
        paired_persons = []
        
        x = len(self.population)
       
        for i in range(x):
            orientation =  temp_list[i].get_orientation()
            if orientation == "Straight":
                temp_straight.append(temp_list[i])
                temp_list[i] = "Assigned"
            elif orientation == "Gay":
                temp_gay.append(temp_list[i])
                temp_list[i] = "Assigned"  
            elif orientation == "Bi":
                temp_bi.append(temp_list[i])
                temp_list[i] = "Assigned"
            else:
                print(temp_list[i].get_orientation())
                print(i)
                print("orientation error")
        while len(temp_bi) != 0:
            r = random.randint(1,10)
            if r > 3:
                partner_i = random.randrange(1,(len(temp_straight)))  
                temp_bi[0].set_partner(temp_straight[partner_i])
                temp_straight[partner_i].set_partner(temp_bi[0])
                paired_persons.append(temp_bi[0])
                paired_persons.append(temp_straight[partner_i])
                del temp_straight[partner_i]
                del temp_bi[0]
            else:
                partner_i = random.randrange(1,(len(temp_gay))) 
                temp_bi[0].set_partner(temp_gay[partner_i])
                temp_gay[partner_i].set_partner(temp_bi[0])
                paired_persons.append(temp_bi[0])
                paired_persons.append(temp_gay[partner_i])
                del temp_gay[partner_i]
                del temp_bi[0]
        while len(temp_gay) != 0:
            partner_i = random.randrange(1,(len(temp_gay))) 
            temp_gay[0].set_partner(temp_gay[partner_i])
            temp_gay[partner_i].set_partner(temp_gay[0])
            paired_persons.append(temp_gay[0])
            paired_persons.append(temp_gay[partner_i])
            del temp_gay[partner_i]
            del temp_gay[0]
            if len(temp_gay) == 1:
                temp_gay[0].set_partner("Single")
                paired_persons.append(temp_gay[0])
                del temp_gay[0]
        while len(temp_straight) != 0:
            partner_i = random.randrange(1,(len(temp_straight)))             
            temp_straight[0].set_partner(temp_straight[partner_i])
            temp_straight[partner_i].set_partner(temp_straight[0])
            paired_persons.append(temp_straight[0])
            paired_persons.append(temp_straight[partner_i])
            del temp_straight[partner_i]
            del temp_straight[0]
            if len(temp_straight) == 1:
                temp_straight[0].set_partner("Single")
                paired_persons.append(temp_straight[0])
                del temp_straight[0]
        if len(paired_persons) == len(self.population):
            self.population = paired_persons
        else:
            print("Old vs New Population mismatch.")
                        
class Person(object):
    def __init__(self):
        #Define key characteristics
        self.age = None
        self.gender = None
        self.first_name = None
        self.last_name = None
        self.alive = None
        #Define social characteristics
        self.orientation = None
        self.parents = []
        self.partner = []
        self.children = []
        #Functions
        self.set_random_age()
        self.set_random_gender()
        self.set_random_name()
        self.set_random_orientation()
    
    #Getters
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    def get_alive(self):
        return self.alive
    def get_orientation(self):
        return self.orientation
    def get_parents(self):
        return self.parents
    def get_partner(self):
        return self.partner
    def get_children(self):
        return self.children

    #setters
    def set_age(self, newage):
        self.age = newage
    def set_gender(self, newgender):
        self.gender = newgender
    def set_first_name(self, newname):
        self.first_name = newname
    def set_last_name(self, newname):
        self.last_name = newname
    def set_alive(self, status):
        self.alive = status
    def set_orientation(self, preference):
        self.orientation = preference
    def set_parents(self, parent_name):
        while len(self.parents) > 1:
            del (self.parents[-1])
        self.parents.append(parent_name)
        self.parents.reverse()
    def set_partner(self, partner_name):
        self.partner = partner_name
    def set_children(self, child_name):
        self.children.append(child_name)
    
    #methods
    def set_random_age(self):
        self.set_age(random.randint(0,100))
    def set_random_gender(self):
        x = random.randint(0,1)
        if x == 0:
            self.set_gender('Male')
        else:
            self.set_gender('Female')
    def set_random_name(self):
        newname = self.generate_random_name()
        #get random_name(gender)
        #returns a list (first name, last name)
        # first_name = random.choice(x)
        # last_name = random.choice(x)
        # print (newname)
        # print (newname[0])
        # print (newname[1])
        self.set_first_name(newname[0])
        self.set_last_name(newname[1])
    def set_random_orientation(self):
        x = random.randint(0,100)
        # 0 is null, 1 is gay, 2 is straight, 3 is bi
        if x in range(2,31):
            self.set_orientation('Gay')
        elif x > 30:
            self.set_orientation('Straight')
        elif x <= 1:
            self.set_orientation('Bi')
        else:
            return str("oops, it broke?")
        
    #function
    def generate_random_name(self):
        gender = self.get_gender()
        #last_name = random.choice(LAST_NAMES)
        first_name = ''
        if gender == 'Male':
            first_name = random.choice(MALE_NAMES)
        elif gender == 'Female': 
            first_name = random.choice(FEMALE_NAMES)
        else:
            print('gender invalid.')
        return [first_name, random.choice(LAST_NAMES)]
        
    def __str__(self):
       return f'{self.name} is {self.age} years old. They identify as {self.gender}, and are {self.orientation}'   

test = Settlement()

