import random
import string

def populate_name_tuple(txt_dir):
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
def populate_name_dict():
    t = [FEMALE_NAMES, MALE_NAMES]
    x = [i for sub in t for i in sub]
    temp_dict = {'unassigned': x,'assigned':[] }
    return temp_dict

FEMALE_NAMES = populate_name_tuple('./names/female/namelist.txt')
MALE_NAMES   = populate_name_tuple('./names/male/namelist.txt')
LAST_NAMES   = populate_name_tuple('./names/last/namelist.txt')
F_M_MASTER   = populate_name_dict()



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
        # self.set_random_age()
        # self.set_random_gender()
        # self.set_random_name()
        # self.set_full_name()
        # self.set_random_preference()
    
    def __repr__(self):
        return f'{self.full_name}|{self.gender}|{self.age}'
    
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
    
    
class Population(object):
    def __init__(self, group_size):
        self.group_size = group_size
        self.population = []
        self.type = ''
        self.families = []
        
    #Getter    
    def get_size(self):
        return self.group_size
    def get_population(self):
        return self.population
    def get_type(self):
        return self.type
    def get_families(self):
        return self.families

    #Setters
    def set_population(self, new_population):
        if isinstance(new_population, list):
            self.population.extend(new_population)
        elif isinstance(new_population, Person):
            self.population.append(new_population)
        else:
            return ValueError
    def set_families(self, new_fam_list=list):
        self.families.append(new_fam_list)
    def set_type(self, new_type):
        #this might be moot if I break groups into broader subclasses
        self.type = new_type
    def set_size(self, newsize=int):
        self.group_size = newsize
        
    #Methods
    def generate_population(self):   
        for _ in range(self.get_size()):
            x = Person()
            self.set_population(x)     
    def generate_families(self):
        pop_unsorted = self.get_population()[:]
        
        while pop_unsorted != 0:
            random.shuffle(pop_unsorted)
            x = Family()
            x.family_size_random()
            x.fam_distribution_calc()
            tempdistrib = x.get_distribution()
            if sum(tempdistrib) > len(pop_unsorted):
                break
            else:
                for i in range(tempdistrib[0]):
                    x.set_parents(pop_unsorted.pop(0))
                for i in range(tempdistrib[1]):
                    x.set_children(pop_unsorted.pop(0))
                for i in range(tempdistrib[2]):
                    x.set_grandparents(pop_unsorted.pop(0))
                for i in range(tempdistrib[3]):
                    x.set_greatgrandparents(pop_unsorted.pop(0))
                self.set_families(x)

    
        '''
        I left off here.
        
        # I need to do getters/setters for Family
        
        in order to generate families I need to pull the distribution val from the Family, and then allot the people to each
        the Family object then needs a method to write to the Person objects in each slot.
        Person objects are going to be blankslates until they are loaded into a container class, ie Family. Family will have methods to flesh out the Person based on the initial distribution.
        This will use the Person setters, so the Person's functionality remains self contained, to be used elsewhere by other classes.
        
        This means that Family might need a few additional attributes & methods: parent preference (which can then be applied to g-parents, etc), & eventually things like race distribution.
        Since these attributes, while stored in the Person class, are key to the general makeup of a Family, their methods will be within Family.
        
        A consideration for Class heirarchy
        Population (currently called group) is a unique class that contains a list of all Families, and all Persons, seperate. It holds key info such as base population, demographics, etc.
        
        Unit(Superclass of Family, not yet made) A Unit will be different compositions of people, ie: Family, Guild, Gang, Extended Family, etc. Things that the superclass will have should be all encompassing: size, type, etc.
            -Family(subclass)
        
        Person - fine as-is, maybe could be broken out by types, Human, elves, etc? might not be needed upfront.
        
        
        '''
        

        
        
    
        
class Family(object):
    def __init__(self):
        self.family_name = random.choices(LAST_NAMES, k = 2)
        self.family_size = None
        self.distribution = None
        self.parents = []
        self.children = []
        self.grandparents = []
        self.greatgrandparents = []
        self.otherpeople = []
    
    #Setters
    def set_family_name(self, lastname=None):
        if isinstance(lastname, None):
            random.choices(LAST_NAMES, k = 2)
        else:
            if isinstance(lastname, list):
                self.fmaily_name.extend(lastname)
            else:
                self.family_name.append(lastname)
        while len(self.family_name) > 2:
            print (self.family_name)
            del self.family_name[input("type index of name to remove:")]
    def set_family_size(self, new):
        self.family_size = new
    def set_distribution(self, distrib):
        self.distribution = distrib
    def set_parents(self, parentlist):
        if isinstance(parentlist, list):
            self.parents.extend(parentlist)
        elif isinstance(parentlist, Person):
            self.parents.append(parentlist)
        else:
            return ValueError
        if len(self.parents) > 2:
            print ('more than 2 parents')
    def set_children(self, childrenlist):
        if isinstance(childrenlist, list):
            self.children.extend(childrenlist)
        elif isinstance(childrenlist, Person):
            self.children.append(childrenlist)
        else:
            return ValueError
    def set_grandparents(self, gparentlist):
        if isinstance(gparentlist, list):
            self.grandparents.extend(gparentlist)
        elif isinstance(gparentlist, Person):
            self.grandparents.append(gparentlist)
        else:
            return ValueError
        if len(self.grandparents) > 4:
            print ('more than 4 grandparents')
    def set_greatgrandparents(self, ggparentlist):
        if isinstance(ggparentlist, list):
            self.greatgrandparents.extend(ggparentlist)
        elif isinstance(ggparentlist, Person):
            self.greatgrandparents.append(ggparentlist)
        else:
            return ValueError
        if len(self.greatgrandparents) > 4:
            print ('more than 4 great grandparents')    
    def set_otherpeople(self, otherpeoplelist):
        if isinstance(otherpeoplelist, list):
            self.otherpeople.extend(otherpeoplelist)
        elif isinstance(otherpeoplelist, Person):
            self.otherpeople.append(otherpeoplelist)
    
    def build_family_members:
        #get last name
        #for parent 1:
            #set preference
            #set gender
            #set name
            #set age
        #for parent 2:
            #p1 preference = p2 pref
            #p2 gender determined by p1 gender + preference
            #set name
            #set age
        #for child in children:
            #set name
            #set age
        #for grandparents
            #for gp1: run parent 1 function
            #for gp2 run parent 1 
    
    #def establish_relations(self):
        #for person in parents:
            #if there are children: set parents children
            #if there are grandparents: set parents parents
        #for children in children:
            #set children parents
        #for grandparents in grandparents:
            #set parents as children
        #for greatgrandparents in _:
            #set grandparents as children
            
    
    #Getters
    def get_family_name(self):
        return self.family_name
    def get_family_size(self):
        return self.family_size
    def get_distribution(self):
        return self.distribution
    def get_parents(self):
        return self.parents
    def get_children(self):
        return self.children
    def get_grandparents(self):
        return self.grandparents
    def get_greatgrandparents(self):
        return self.greatgrandparents
    def get_otherpeople(self):
        return self.otherpeople
    def get_whole_family(self):
        return f'{self.parents},{self.children},{self.grandparents},{self.greatgrandparents}'
    
    def family_size_random(self):
        x = random.choices(range(1,16), weights=(1,15,30,50,50,50,50,50,30,20,10,5,5,4,3), k = 1)
        self.set_family_size(x[0])
        

    def fam_distribution_calc(self):
        self.distribution = []
        temp_list = {'c':[0,0.66], 'gp':[0,0.26], 'ggp':[0,0.13] , 'o':[0,0]}
        parentval = random.choices([1,2], weights=(1,99), k = 1)
        self.distribution.append(parentval[0])
        
        def determine_y (current_distrib, yfrac, size):
            cdsum = sum(current_distrib)
            if len(current_distrib) == 0:
                return 2
            else:
                y = round(yfrac*size)
                while y+cdsum > size:
                    y -= 1
                if y <= 0:
                    return 0
                else:
                    return y  
        
        for key in temp_list:
            z = temp_list.get(key)
            x = z[0]
            yfrac = z[1]
            self.distribution.append(random.randint(x,determine_y(self.distribution, yfrac, self.family_size)))
        
        
  
    
  
    
# def fam_distribution_calc(size):
#     temp_distrib = []
#     temp_list = {'c':[0,0.66], 'gp':[0,0.26], 'ggp':[0,0.13] , 'o':[0,0]}
#     parentval = random.choices([1,2], weights=(1,99), k = 1)
#     temp_distrib.append(parentval[0])
#     def determine_y (current_distrib, yfrac, size):
#         cdsum = sum(current_distrib)
#         if len(current_distrib) == 0:
#             return 2
#         else:
#             y = round(yfrac*size)
#             while y+cdsum > size:
#                 y -= 1
#             if y <= 0:
#                 return 0
#             else:
#                 return y  
    
#     for key in temp_list:
#         z = temp_list.get(key)
#         x = z[0]
#         yfrac = z[1]
#         temp_distrib.append(random.randint(x,determine_y(temp_distrib, yfrac, size)))
        
#     print(temp_distrib)
