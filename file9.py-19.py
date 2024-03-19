
'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number



#eg:3
def profile(name,age,palce):
    txt = "my name is {}.iam {} years old. iam from{}."
    print(txt.format(name,age,place))
profile("pradeep",20,"cbe")


# ! eg:4
# ? function with return statement

# return
#1.) A variable declared inside the function can be accessed outside the function
#using return
# 2.) return does not print anything
#3.)we cannot write any code below return statement


def f1():
    z = 8
f1()
print(z) # error ----> cannot use outside the function




def f1(a,b):
    c = a*b
    return c
f1(6, 8)
# print(f1(6,8)
obj = f1(6,8)
obj1 = f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)



# ? problem:1

def palidrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        p[rint(n,"palindrome:")
    else:
        print("Not palindrome")
a = int(input("enter the value:")
palindrome(a)




# ? Based on the decleration of parameter and args
# ? functions are divides into 6 catagories

# Positional args
# Keyword args
# default args
# variable length args
# Keyword variable length args


# # * positional args
# ? The position of para meter have to be same as position os arguments

# ! Eg:1
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}.i got {} marks."
    print(txt.format(name, phone, mark))

profile("pradeep", 9347937582, 99) # unexpected output


# * keyword args
# ! eg:2

# ? To overcome the disadvantage of position args, we use keyword args
# ?it is the process of intialising the parameter with the args while calling the
# ? function
 
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}.i got {} marks."
    print(txt.format(name, phone, mark))

profile(name = "pradeep", mark=96,phone=9347937582)



# todo -----> exception of keyword args function
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}.i got {} marks."
    print(txt.format(name, phone, mark))

# profile(name="pradeep, 9347937582, mark=98) # error
# profile(9347937582, name="pradeep", mark=98) # error

profile("pradeep", mark=99, phone=9347937582)


# * Default args

# The method of assigning the argument to the parameter while declaring the
# function

# ! eg:1
def profile(name,phone,"nandyal"):
    txt = "my name is {}. my phone number is {}.i am from {}."
    print(txt.format(name, phone, place))

profile("sid", 9347937582, "nandyal")



def profile(name,phone, place="nandyal"):
    if place == "kadapa" or place=="kadapa or place=="kadapa":
        txt = "my name is {}. my phone number is {}.i am from {}."
        print(txt.format(name, phone, place))
    else:
        print("you are not eligible to signup")
        profile("sid", 9347937582, "kadapa")



# ! Exception

def profile(name, place="nandyal" phone): # error ----> coz default args should not follow
                                          # positional param
    if place == "kadapa" or place=="kadapa or place=="kadapa":
        txt = "my name is {}. my phone number is {}.i am from {}."
        print(txt.format(name, phone, place))
    else:
        print("you are not eligible to signup")
        profile("pradeep", 9347937582, "kadapa")




# ! variable length parameters
# !Eg:1
# to pass more than 1 arg to a para meter means we use variable length args
# to covert normal parameter to variable length param, add* * to their prefix of param

# name = "pradeep", 'name2', 'name3'
def profile(*name):
    for val in name:
        print("my name is",name)
profile("sid", 'name2', 'name3')



# ! Eg:2

def profile(*name,age):
    for val in name:
        print("my name is",val, "my age is", age)
profile("sid", 'name2', 'name3',28) # error ----> age has no args



def profile(age, *name):
    for val in name:
        print("my name is",val, "my age is", age)
profile( "pradeep", 'ravi', 'sampath')
profile(24,34,23)





# * keyword variable length args
# Kwargs ----> which is used to provide the args in the form of keyvalue pair

#! Eg:1

def price(**price_list):
    print(price_list)

price(shirt=1000, realme=12000)


# n = 5
#{1:1, 2:4, 3:9, 4:16,5:25}

n = int(input("enter the values:"))
d1 ={}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)


def dict1(n):
    d1 ={}
    for val in range(1, n+1):
        d1[val] = val**2
    print(d1)
dict1(5)

    
# ! --------> object oriented programming


The panadigms of objects oriented programming are
# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation


# ! class is a blue print of an object

l1 = [1,2,3,4,5,6]

# ? Eg:1
class c1:
    name1 = "pradeep"
    print(name1)

# ? Eg:2
class person:
    name1 = "pradeep"

c = person() # c os object
# the process of creation of an object is called instantiation
print(c.name)

'''

# ? eg:3

# create of a method

# when the function is created with a class is called as method

class person:
    def display(person): # it is a method
        print("hello welcome to classes")

p = person()
p.display()

# ? Eg:4
# ! method with para meter
class person:
    def display(person,name,age):
        pass

p = person()
p.display("pradeep",20)




















#d1 = {"a":100, "b":200, "c":300}
#d1 = dict(a=100, b=200, c=300)
#print(d1)

























