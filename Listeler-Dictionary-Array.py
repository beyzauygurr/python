# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:20:13 2024

@author: HP
"""
#LISTS

mylist=["a","b","c"]
print(mylist)
print(len(mylist)) #length

#lists can contain different data types
 
list=["abs",43,True,34.43]
print(list)
print(type(list)) #list

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

mylist=["red","yellow","blue","orange"]
print(mylist[2]) #acces items -blue
print(mylist[-2]) #blue
print(mylist[1:3]) #position3 is not included
print(mylist[:2])
print(mylist[2:])

mylist[1]="purple" #change item value
print(mylist) 
mylist.insert(2,10.9) #insert 10.9 at position 2
print(mylist)

mylist.append(10)
print(mylist) #append 10

mylist.remove(10)
print(mylist) #remove 10

mylist.pop(1) #remove specified index
print(mylist) 

mylist1=["1","2"]

list=mylist+mylist1
print(list)

#SETS

thisset = {"apple", "banana", "cherry"}
print(thisset)

#DICTIONARY

dict={
      "brand":"mercedes",
      "model":"C180",
      "year":1993
      }

print(dict)
print(dict["model"])
x=dict.get("year")
print(x)
y=dict.values()
dict["year"]=1990
print(y)
dict.update({"year":2020})
print(dict)
dict.update({"color":"red"})
print(dict)
dict.pop("color")
print(dict)







