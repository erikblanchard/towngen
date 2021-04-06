# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:41:38 2021

@author: ErikB
"""

#FemaleNames = open("./names/female/namelist.txt", 'r').readlines()

import random
import string

def populateNameList(txtdir):
    #import string
    result = sorted(set(
    word.strip(string.punctuation)
    for line in open(txtdir)
    for word in line.split()))
    return result

FemaleNames = populateNameList('./names/female/namelist.txt')
MaleNames = populateNameList('./names/male/namelist.txt')
LastNames = populateNameList('./names/last/namelist.txt')

# def RandomNameOriginal():
#     '''
#     Original RandomName that asks the user for input to determine sex.    
#     '''
#     import random
#     FullName = ""
#     def NameCompilation(x):
#         RName = random.choice(x)
#         LName = random.choice(LastNames)
#         FullName = RName + ' ' + LName
#         return FullName.title()     
#     while FullName == "":
#         charSex = input('What Sex is your Character, Male, Female, or Either: ')
#         if charSex.lower() == 'male':
#             print("Your Character's name is: ", NameCompilation(MaleNames))
#             break
#         elif charSex.lower() == 'female':
#             print("Your Character's name is: ", NameCompilation(FemaleNames))
#             break    
#         elif charSex.lower() == 'either':
#             print("Your Character's name is: ", NameCompilation(FemaleNames + MaleNames))
#             break     
#         else:
#             print("Hmm, seems like you typed some bullshit in there, try again and don't fuck up...")   

def RandomName(x, LName):
    
    FullName = ""
   
    while FullName == "":
        charSex = x
        if charSex.lower() == 'male':
            return NameCompilation(MaleNames, LName)
        elif charSex.lower() == 'female':
            return NameCompilation(FemaleNames, LName)
            break    
        else:
            return NameCompilation(FemaleNames + MaleNames, LName)
            break     
        
def NameCompilation(x, LName):
       RName = random.choice(x)
       #LName = random.choice(LastNames)
       FullName = RName + ' ' + LName
       return FullName.title()     
            
def FamilyUnit():
    
    x = ''
    FamSize = random.randint(3,10)
    Family = []
    xdetermine = 0
    LName = random.choice(LastNames) 
    
    for person in range(FamSize):
        xdetermine = random.randint(1,3)
        if xdetermine == 1:
            x = 'male'
        elif xdetermine == 2:
            x = 'female'
        else:
            xdetermine = 'either'
        Family.append(RandomName(x, LName))
    return Family 

def RoleAssignment():
    
    GayChance = random.randint(0,100)
    if GayChance > 30:
        return FamDistributor(0)
    else:
        return FamDistributor(1)
    
    
def FamDistributor(distribval):
    
    Family = FamilyUnit()
    Dad = []
    Mom = []
    Kids = []
    
    for FamilyMember in Family:
        if FamilyMember.upper().split()[0] in MaleNames:
            if len(Dad) > distribval or len(Mom) > 1:
                Kids.append(FamilyMember)
            else:
                Dad.append(FamilyMember)
        else:
            if len(Mom) > distribval or len(Dad) > 1:
                Kids.append(FamilyMember)
            else:
                Mom.append(FamilyMember)
   
    FamilyGroup = {"Dad":Dad, "Mom":Mom, "Kids":Kids}
    return FamilyGroup

def ManyFamilies():
    numFam = range(10)
    Community = []
    Counter = 0
    
    for i in numFam:
        Counter += 1
        #Community.append(str("Family"+str(Counter)+":"))
        Community.append(RoleAssignment())
    return Community
    #print(Community)
        
    
    #if len(Dad) + len(Mom) == 2:
    #    print (*Dad, "and ", *Mom, ' have ', len(Kids), 'kids. Their names are: ', ', '.join(Kids))
    #elif len(Dad) == 0 and len(Mom) == 1:
    #    print (*Mom,'raises her children,', ', '.join(Kids), 'alone.')
    #elif len(Mom) == 0 and len(Dad) == 1:
    #    print (*Dad,'raises his children,', ', '.join(Kids), 'alone.')
    #else:
    #    print (*Mom, *Dad, ', '.join(Kids), 'idkidktest')
    
    #print(len(Mom), len(Dad), 'TestVALUES')           
    