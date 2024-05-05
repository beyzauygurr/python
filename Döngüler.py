#WHILE LOOP

beyza=1
while beyza<25:
    print(beyza)
    beyza+=1


i=0
while i<=10:
    print(i)
    if i==5:
        break #with the break statement we can stop the loop
    i+=1
    
print("++++++")

b=0
while b<9:
    b+=1
    if b==3:
        continue #print without 3
    print(b)
    

#FOR LOOP

#for loop is used for iterating over a sequence(list,tuple,dict,set,string)

fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    
    
for x in "banana":
    print(x)
    
    
for x in range(6):
    print(x) #values 0 to 5.
    
print("$$$$$$$$$$")
    
for x in range(2,6):
    print(x) #values 2 to 5.
    
print("$$$$$$$$$$")

for x in range(2, 30, 3):
  print(x)
    
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
#NESTED LOOPS

color=["red","yellow","blue"]
fruits=["apple", "banana", "cherry"]

for x in color:
    for y in fruits:
        print(x,y)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    