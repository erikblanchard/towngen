# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:15:48 2021

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


child_age = range(0,20)
young_age = range(0,13)
teen_age = range(13,20)
adult_age = range(20,66)
elderly_age = range(65,120)


class Group(object):
    def __init__(self):
        self.size = None
        self.name = None
        #name of group, "The Johnson Family", "Thieves Guild"
        self.people = []
        self.descriptor = None
        #type can be a family, a club, a guild; a nonregional descriptor
        self.has_relationships = False
        #Boolean to determine if people in group are paired 
        self.age_groups = []
        #define age groups which will be used in generate_people function.
        
    #Getters
    def get_size(self):
        return self.age
    def get_name(self):
        return self.name
    def get_people(self):
        return self.people
    def get_descriptor(self):
        return self.descriptor
    def has_relationships(self):
        return self.has_r
    def get_age_groups(self):
        return self.age_groups
    
    #Setters
    def set_size(self, size_int):
        self.size = size_int
    def set_name(self, new_name):
        self.name = new_name
    def set_people(self, Person):
        self.people.append(Person)
    def set_(self, type_str):
        self.type = type_str
    def set_has_relationships(self, boolean=False):
        self.has_relationships = boolean
    def set_age_groups(self, age_group_list):
        #child, teen, adult, elderly. these are obj.
        self.age_groups.extend(age_group_list)
        
    def generate_people(self, size, relationship_type):
        new_group = []  
        for _ in range(size):
            new_person = Person()
            new_group.append(new_person)
        
                    #determine relationship type
                    #determine appropriate relationship for current Person
                        #if relationship has limit (i.e. only 2 parents) check against current new_group
                    #call relationship_pairing with appropriate information
                        #type, current new_person, new_group, 
    
    #def relationship_pairing(self, relationship_type):
        #take in relationship type
            #if x relationship return x_relationship_function()
        
    def relationship_family(self):
        temp_list = self.people[:]
        family = []

        while len(temp_list) != 0:    
            while len(family) == 0:
                for i, person in enumerate(temp_list[1:],1):
                    if temp_list[i].get_gender() in temp_list[0].get_preference():
                        temp_list[0].set_age(random.choice(adult_age))
                        temp_list[0].set_partner(person)
                        temp_list[i].set_partner(temp_list[0])
                        temp_list[i].set_age(
                            random.randint(round((temp_list[0].get_age() + 20) / 2 ), temp_list[0].get_age() + 10)
                            )
                        temp_list[i].set_preference(temp_list[0].get_gender())
                        temp_list[i].set_last_name(temp_list[0].get_last_name())
                        family.append(temp_list.pop(i))
                        family.append(temp_list.pop(0))
                        print(family[0].get_full_name(), family[0].get_age(), family[1].get_full_name(), family[1].get_age())
                        break
                    else:
                        print(f'no match {i}, {temp_list[i].get_gender()} is not in {temp_list[0].get_preference()}')
                        
            while len(family) >= 2 and len(family) < 10:
                #set children, currently doesn't handle set_siblings
                temp_list[0].set_age(random.choice(child_age))
                temp_list[0].set_parents(family[0])
                temp_list[0].set_parents(family[1])
                family[0].set_children(temp_list[0])
                family[1].set_children(temp_list[0])
                temp_list[0].set_last_name(family[0].get_last_name())
                family.append(temp_list.pop(0))
                
                
            while len(family) >= 10 and len(temp_list) > 0:
                
                # if temp_list[0].get_age() >= 120:
                #     print (f'{temp_list[0].get_name()} is dead, they were {temp_list[0].get_age()}')
                #     del temp_list[0]
                if len(family[-1].get_children()) == 0:
                    # Set parent1 of parent1 @ family[0]
                    temp_list[0].set_age(random.randint(
                    family[0].get_age() + 18, family[0].get_age() + 60
                    ))
                    temp_list[0].set_last_name(family[0].get_last_name())
                    temp_list[0].set_children(family[0])
                    family[0].set_parents(temp_list[0])
                    family.append(temp_list.pop(0))
                    break
                if len(family[-1].get_children()) != 0:
                
                    if len(family[-2].get_children()) == 0:
                        # Set parent1 of parent2 @ family[1]
                        temp_list[0].set_age(random.randint(
                        family[1].get_age() + 18, family[1].get_age() + 60
                        ))
                        #temp_list[0].set_last_name(family[0].get_last_name())
                        temp_list[0].set_children(family[1])
                        family[1].set_parents(temp_list[0])
                        family.append(temp_list.pop(0))
                        break
                    elif len(family[-3].get_children()) == 0:
                        # Set parent2 of parent1 @ family[0]
                        temp_list[0].set_age(
                            random.randint((family[0].get_age() + 18), (temp_list[-2].get_age() + 10))
                            )
                        temp_list[0].set_last_name(family[0].get_last_name())
                        temp_list[0].set_children(family[0])
                        temp_list[0].set_partner(family[-2])
                        family[-2].set_partner(temp_list[0])
                        family[0].set_parents(temp_list[0])
                        family.append(temp_list.pop(0))
                        break
                    elif len(family[-4].get_children()) == 0:
                        temp_list[0].set_age(
                            random.randint(family[1].get_age() + 18, temp_list[-2].get_age() + 10)
                            )
                        temp_list[0].set_last_name(family[-2].get_last_name())
                        temp_list[0].set_children(family[0])
                        temp_list[0].set_partner(family[-2])
                        family[-2].set_partner(temp_list[0])
                        family[0].set_parents(temp_list[0])
                        family.append(temp_list.pop(0))
                        break
                    else:
                        del temp_list[0]
                        break
                    break
        
        self.people = family
                        
                
            #while len(family) in 
                        
                        
                        
        #take list of people and:
            #designate parents:
                #read preference, designate second parent based on that.
                #choose last name, which we will apply to all Persons
                #set age for both within range(adult) +/- 10 years apart
                #append name to each under partner
                #add name to new_list
                
            #designate children
                #set preference to None
                #set last name
                #set age within range(child, teen) unless parents are over 55, add +10
                #append parent names, and
            
            #if size of list_people > 10, assign grandparents:
                #if woman, grandma1, if man grandpa1:
                    #set age elderly
                    #read preference, designate 2nd grandparent
                        #if no viable 2nd parent, next grandparent will maintain their last name
                    #adjust last names
                    #append names to one of the parents, random choice
            
            #if parents selected, children maxed, and no viable grandparents, delete remaining names.

#    def age_distrib(family,size,age_groups):
        


# class Family(Group):
               
#     # def __init__(self, hasrelationships=True):
#     #     self.descriptor = 'family'
#     #     self.hasrelationships = True
#     #     #self.partner_preference = None
#     #     super().__init__()
#     #     #Male, Female, or Both
        
        
        
        

class Person(object):
    def __init__(self):
        #Define key characteristics
        self.age = None
        self.gender = None
        self.first_name = None
        self.last_name = None
        self.full_name = None
        self.alive = None
        #Define social characteristics
        self.preference = []
        self.parents = []
        self.partner = []
        self.children = []
        self.siblings = []
        #Functions
        self.set_random_age()
        self.set_random_gender()
        self.set_random_name()
        self.set_full_name()
        self.set_random_preference()
    
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
        self.set_full_name()
        return self.full_name
    def get_alive(self):
        return self.alive
    def get_preference(self):
        return self.preference
    def get_parents(self):
        return self.parents
    def get_partner(self):
        return self.partner
    def get_children(self):
        return self.children
    def get_siblings(self):
        return self.siblings

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
    def set_preference(self, newpreference):
        self.preference.clear()
        if type(newpreference) == list():
            self.preference.extend(newpreference)
        else:
            self.preference.append(newpreference)
    def set_parents(self, parent_name):
        while len(self.parents) > 1:
            del (self.parents[-1])
        self.parents.append(parent_name)
        self.parents.reverse()
    def set_partner(self, Person):
        self.partner = Person
    def set_children(self, Person_list):
        self.children.append(Person_list)
    def set_full_name(self):
        self.full_name = self.first_name + ' ' + self.last_name
    def set_siblings(self, Person):
        self.siblings = Person
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
        self.set_full_name()
    def set_random_preference(self):
        x = random.randint(0,100)
        # 2-30 is gay, 31+ is straight, 0-1 is bi
        if x in range(2,31):
            if self.gender == 'Male':
                self.set_preference('Male')
            elif self.gender == 'Female':
                self.set_preference('Female')
        elif x > 30:
            if self.gender == 'Male':
                self.set_preference('Female')
            elif self.gender == 'Female':
                self.set_preference('Male')
        elif x <= 1:
            self.set_preference(['Male','Female'])
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
    
    
    
    

grouptest = Group()

for _ in range(15):
    person = Person()
    grouptest.set_people(person)

for i in range(15):
    print(grouptest.people[i].get_full_name())
    print(grouptest.people[i].get_gender())
    print(grouptest.people[i].get_preference())
    
grouptest.relationship_family()

for i in range(len(grouptest.get_people())):
    print(len(grouptest.get_people()))
    print(
        f'{grouptest.people[i].get_full_name()}, age: {grouptest.people[i].get_age()}, parents:{grouptest.people[i].get_parents()}, children:{grouptest.people[i].get_children()}, gender:{grouptest.people[i].get_gender()}, preference:{grouptest.people[i].get_preference()}'
        )
    