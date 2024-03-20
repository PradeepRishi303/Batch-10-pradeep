'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number


s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.spilt(" ")
s2 = s2.spilt(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)



# 3.) write a code print the 8th fibanochi number

# 0,1,1,2,3,5,8

num = 5
n1 = 0
n2 =1

n1 = 1
n2 = 1
ans = 1+1 ===>3

n1 = 2
n2 = 3
ans = 2+3=5



num = 5
n1 = 0
n2 = 1

for val in range(5):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)



# ! constructors

# ? Eg:2

class profile:
    def __init__(self):
        print("hello world")

obj = profile()
obj.__init__()


# ? Eg:3

# * parametarised constructor
class profile:
    def__init__(self,id,name,age):
        print(id,name,age)

obj = profile(1,"pradeep",20)




# ? Eg:4
class c1:
    email = "akulapradeep42@gmail.com"
    
    def m1(self):
        name = "pradeep"
        place= "cbe"
        print(name,place)
        print(self.email)

object = c1()
object.m1()


# ? Eg:5
class c1:
    def m1(self):
        name = "pradeep"
        age = 20
        return name, age
    def display(self):
        # print(name, age)
        # print(self.mame, self.age)
        print(m1())
        

        
object = c1()
object.display()




# ? eg:6
# ? To use the variable inside the constructor in another words
class class1:
    def__init__(self):
         name = "pradeep"
         email = "pradeep@gmail.com"  # static variable  
         # return name, email  # error ---> use return with constructor
    
         
    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()


# ! -----Inheritance

# The process of utilising the methods and attributes of parent class
# through the object of child class it is called as inheritance

# 5 types of inheritance
---> single
---> multilevel
---> multiple
---> hybrid
---> heirarichal


# * single inheritance
# ? it has only one parent class only one child class
# ! eg:1

class parent:
    def m1():
        print("iam parent class")

class child(parent):
    def m2(self):
        print("iam child class")

obj = child()
obj.m1()


#! eg:2
class c1:
    def __init(self):
        print("i am constructor from parent class")

class child(c1):
    pass

obj = child1()


#! Eg:3
class patent:
    name = "pradeep"

class child(parent):
    name = "name1"
    
    def display(self):
        print(self.name)
        
d = child()
d.display()



# ! multilevel inheritance

# ? Eg:1
class voice:
    def sound(self):
        print("all the animals have their own voices")

class dog(voice):
          def dog_voice(self):
              print("bark")

class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()



# ? EG:2

class honda_city:
    def engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(self, cc, hp, torque, fuel_type, num_of_piston)

        def body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class amaze:
        def amaze_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def amaze_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class civic(amaze):
        def civic_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def civic_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class honda:
    pass

honda= Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")




# ! multiple inheritance
# ? it has multiple parent and 1 child



class while_petrol:
    def function1(self):
        print("used to Airplans")

class organic_petrol:
    def function_o(self):
        print("used for bike, cars")

class premium_petrol:
    def function_p(self):
        print("sports car, bikes")

class petrol(white_petrol, organic_petrol, premium_petrol):
    def defanition(self):
        print("petrols type")

p=petrol()
p.defanition()
p.function_o()



# ! eg:2
class addition:
    def add(self, a, b):
        print(a+b)

class subtract:
    def sub(self, a, b):
        print(a-b)

class multiply:
    def mul(self, a, b):
        print(a*b)

class division(addition, subtract, multiply):
    def div(self, a, b):
        print(a/b)


calc = division()
calc.add(3, 4)
calc.mul(5,2)



# ! heirarical inheritance

# MRO --> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
        
    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
        
calc = division() 
# calc.add(3, 4)
calc.mul(4, 2)




# ! Heirarical inheritance

#? The one parent classe will asct as parent for all the child classes
class catagory:
def weight(self, weight): print(weight)
I
def display(self, color, taste): print(color, taste)
class Tomato(catagory):
def tomato_specs (self):
color="black"
taste "neutral taste"
self.display(color, taste)
class carrot (catagory):
def carrot_specs (self):
color="green"
LF-321


# ! hybrid inheritance
# ? The combination of above 4 inheritance is called hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2(c1):
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("Class 3")
class c4(c3):
    def m4(self):
        print("Class 4")
class c5(c4):
    def m5(self):
        print("Class 5")
class c6(c5):
    def m6(self):
        print("Class 6")



'''
# ! ------> polymorphism
# ? poly - many, morph ---> form
# A function which has the ability to perform more than 1 functionality
# then it is considered to be as plioymorphism

# * ploymorphism in built in functions

# len() ---> which is used to find the length of list, tuple, dict etc..
# index()
# max()
# min()
# count()
# pop()

# * ploymorphism in operations



# +
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

# *
l1 ={12,3,4,5,6}
print(*11)
def f1(*args):

l1 = [1,2,3,4]
print(l1*10)




        
 



    
