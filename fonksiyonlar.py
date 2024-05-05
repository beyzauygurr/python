#FUNCTION

def func():
    print("hello")
    
func()


def my_func(name): 
    print(name)
    
my_func("beyza") #argument
my_func(2)

"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(food):
    for x in food:
        print(x)
        
fruits=["apple","banana", "cherry"]
my_function(fruits)

def my_function(x):
  return 5 * x #To let a function return a value, use the return statement:

print(my_function(3))
print(my_function(5))
print(my_function(9))


#kullanıcıdan alınan sayının faktöriyelini hesaplayan fonk

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
numb=int(input("enter a number:"))
print(factorial(numb))
























