#!/usr/bin/env python3

def greet_programmer():
    
    print ("Hello Programmer!")
 
 
def greet(name= "Naureen"):
    print(f"Hello {name}")
    

def greet_with_default(name="programmer"):
    print ()
    print("Sunny!")
    

def add(num1=1, num2=2):
    return(num1+num2)
    

    

def halve(number):
    return number / 2 if isinstance(number, (int, float)) else None


print(halve(4))      
