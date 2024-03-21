#Assessment:
#1.)Python program to captilalize the first and last character of each word in a string
#2.)Input:128
#ouput:Yes
#128%1==0,128%2==0, and 128%8==0.
#3.)l1=[1,2,3,4],l2=[5,6,7,8]
#add both l1 and l2 and ans=[6,8,10,12]

#1.)
'''s1="hello world"
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)'''

'''s1="hello world"
print(s1.replace("h", "H"))
print(s1.replace("d", "D"))'''

#2.)
n=128
'''while n!=0:
    rem = n%10
    print(rem)
    n = n//10'''
'''for i in str(n):
    print(i)'''
'''temp=n
f1=0
while n!=0:
    rem = n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
if f1==0:
    print("yes")
else:
    print("no")'''

#3.)
#l1=[1,2,3,4]
#l2=[5,6,7,8]

'''print(l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])'''
#l3=[]
'''for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)'''

# Characteristics of set
#1.) Set can be created using {}
#2.) The elements inside set are not indexed
#3.) Does not allow duplicate values
#4.) It unordered
#5.) Heterogenous
#6.) Mutable or changable

#Eg:1
'''s1={9,89,7.76,8+7j,(8,7,5),"truck","e"}
print(s1)
'''

#Eg:2
'''s2={5,8,98,[9,0]}
print(s2)---> error'''

#Eg:3
#min(), max(), len()

#Eg:
# To add elements inside set
#s1={8,78,67,"u"}
#add()
'''s1.add(43)
print(s1)'''

'''s1.update([9,0])
print(s1)'''

# To delete the elements inside set
#s1={8,78,67,"u"}
#pop()----> to delete one random element

'''s1.pop()
print(s1)
'''

#remove---> to remove one specific element
'''s1.remove(78)
print(s1)'''

#discard()
'''s1.discard(8967)
print(s1)'''

#clear()--->
'''l1=[]
print(type(l1))''' #---> list

'''l1={}
print(type(l1))''' #---> dict

#s1=set() # to create empty set
'''print(type(s1))''' #----> set

'''s1={8,9,0}
s1.clear
print(s1)'''

'''del s1
print(s1)'''

# JOin the sets
'''s1={9,8,7}
s2={9.90,"card","t", 56}
#union()---> to combine 2 sets
s3=s1.union(s2)
print(s3)'''

# intersection ---> to get common elements
'''s1={4,5,6}
s2={5,6,7,8}
print(s1.intersection(s2))'''

# difference ---> to get different elements in the set
'''s1={4,5,6}
s2={5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))'''

#isdisjoint(), issubset(), issuperset()
''''
s1={8,9,0}
s2={6,7,8,9,0}
print(s1.issubset(s2))
print(s1.issuperset(s1))
'''

#---> Problem:1
'''s1={1,2,3,4,5}
s2={3,2,7,8,9}
#n1={1,2,3}--->s1
for val in s1:
    if val in s2:
        print("its a joint set")
    
for val in s1:
    if val in s2:
        str1="its a joint set"
print(str)'''

# ? o/p---> its a joinset
# dictionary---> how many group of elements in a list
#Eg:1
d1={1:100, "a":200, 4.5:"hello"}
marks_stud1={"English":79, "maths":20, "physics":60}

'''print(d1)
print(len(d1))'''

# char of dictionary
#1.) have to be surrounded bt{}
#2.) It have to be in the form of key, value pair
#3.) It is mutable
#4.) Duplicate keys are not allowed, duplicate values are allowed
#5.) It is ordered
#6.) Key does not allow mutable datatypes, values allow mutable datatype
#7.) It is unindexed

# To access elements in dictionary
#d1={1:100, 2:200, 3:300, 4:400}

#print(d1)
#or
# To access the values, have to use key
'''print(d1[1])''' #---> 100

#some common functions
#len(), min(), max()
'''print(min(d1))
print(max(d1))'''

# To find min, max based on values
'''print(min(d1.values()))
print(max(d1.values()))'''

# dictionary based functions
# To add element(key and value pair) in dict
'''d1={1:100, 2:200, 3:300, 4:400}
d1[5]=500
print(d1)'''

# To replace a value in dictionary
'''d1={1:100, 2:200, 3:300, 4:400}
d1[2]="mango"
print(d1)'''

#delete elements from dictionary
#d1={1:100, 2:200, 3:300, 4:400}
#poptem() ----> to delete the last key value in dictinary
'''d1.popitem()
print(d1)'''

#pop()
'''d1.pop(2) # 2 is the key in dictionary 
print(d1)'''

#clear(), del
#join 2 dictionary
#update()
'''d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple", "b":"boy", "g":"game"}
d1.update(d2)
print(d1)'''

# get()--> used to get the value from a key
d1={1:100, 2:200, 3:300, 4:400}
'''print(d1[3])
print(d1.get(3))
print(d1.get(90))'''


# To print all the keys()
'''print(d1.keys())
print(type(d1.keys()))'''

# To print all the values
'''print(d1.values())'''

# Iterating dictionary
'''for val in d1:
    print(val)'''

'''for val in d1.values():
    print(val)'''

# To get both keys and values
'''for key, val in d1.items():
    print(key,val)'''

# Problem:1

'''
n=int(input("enter num of times: "))
integer=[]
float_value=[]
string=[]
for val in range(n):
    value = eval(input("enter the value"))
    if type(val)==int:
        integer.append(val)
    elif type(val)==float:
        float_value.append(val)
    elif:
        string.append(val)
    else:
        print("pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
'''

# Problem:2
# Return a set of elements present in set A or B, but not both
#set1={10,20,30,40,50,}
#set2={30,40,50,60,70}
#o/p={20,70,10,60}


#set1={10,20,30,40,50,}
#set2={30,40,50,60,70}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

'''l1=set1 ^ set2
print(l1)'''


set3=set()
'''for val in set1:
    if val not in set2:
        print(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)
'''
#---> Problem:3
l1=[1,2,3,4]
l2=["a","b","c","d"]
'''
d1={}
d1[l1[0]]=l2[0]
d1[l1[1]]=l2[1]
d1[l1[2]]=l2[2]
d1[l1[3]]=l2[3]
print(d1)
'''

'''
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)
'''



# ! or
'''
c = 0
for val in set1, set2:
    c=c+1
    if c==1:
        for element in val:
            if element not in set2:
                set3.add(element)
    elif c==2:
        for element in val:
            if element not in set1:
                set3.add(element)
print(set3)
'''

#1.) swap elements in string list
# The original list is :["Ggf", "best", "for", "Geeks"]
# List after performing character swaps:]"efg", "is", "bGst", "for", "eGGks"]


# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}

#  3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']
