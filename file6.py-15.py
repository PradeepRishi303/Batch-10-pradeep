
'''

# ! ------> commom functions for list

l1 = [6,7,8,9,0]
# print(len(l1))

print(max(l1))
print(min(l1))



l1 = [6,7,8,9,"p","u"]
print(max(l1))
print(min(l1))


l1 = [6,7,9,0,8.89,-5,0.78]
#index() ---> to get the index value of specific element
print(l1.index(9))


l1 = [6,7,9,0,8.89,-5,0.78]
# count() ----> how many num of times an element is repeated
print(l1.count(6))



#! some functions which is specifically used  for list

#To add element inside list
# ? insert ()---> to add element at specific index position

l1 = [6,7,9,0,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)



# ? To delete element from list
l1 =[6,7,9,0,8.89,-5,0.78]
# pop() ----> last element will be deleted
l1.pop()
print(l1)



# pop(index_value)---> used to delete element at specific index value
l1.pop(4)
print(l1)



# remove(element) ---> used to delete element in list

l1 =[6,7,9,0,8.89,-5,0.78]
l1.remove(8.89)
print(l1)




#* clear() ---> to complete delete all element in list
l1 =[6,7,9,0,8.89,-5,0.78]
l1.clear()
print(l1)



# del ---> to delete the list

l1 =[6,7,9,0,8.89,-5,0.78]
del(l1)
print(l1)




# ? ----> join 2 lists

l1 = [9,0,8]
l2 = ["p","0","t",34]
#print(l1+l2)

# or
l1.extend(l2)
print(l1)


# ? ------> copy()
l1=[6,7,8,9,3,]
l2=l1.copy()
#print(l2)
#print(l1)

print(id(l1))
print(id(l2))


# ! diff between shallow copy and deep copy
# shallow copy,
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)


# deep copy
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
# print(l1[-1][1]) -----> to index nested list


l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)



# ? sort ---> arrange elements in list in ascending or desending
l1 = [9,7,45,0,-6,5,12]
#l1.sort()
#print(l1)

# l1.sort(reverse=true)
# print(l1)

#l1 = ['z','i','0','p']
#l1.sort()
#print(l1)

# list constructor
list()
l3 = ((8,9,0))
print(list(13))


# ----> nested list
l1 = [8,9,[0,8,7],["p","o",'y'],[8,'t']]
# print(l1[-2][1]) .......> 0

#print(l1[1:4])
#print(l1[1:-1])



# ? to delete "t" from l1

#print(l1[1:-1]). remove('t')
#print(l1)

# ? combine these ["p","o",'y'],[8,'t'] lists in l1 to "p","o",'y',8,'t']

l1 = ['p','o','y']
l2 = [8,'t']
l1. extend (l2)
print(l1)



# ! ------> Tuple
# 3 * char of tuple

#1.) tuple have to be surrounded by ()
#2.) The elements inside tuple are npt changable
#3.) The elements inside tuple are indexted
#4.) The element will execute in order
#5.) it is heterogenous
#6.) it allow duplicate elements

#eg:
t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))


# ? indexing, slicing are all same as list

# ways to create tuple
l1 = (8)
print(type(l1))  # int

l1 = (8)
print(type(l1))  # tuple


t1 = 8,9
print(type(t1))

t2 = 8,
print(type(t2))



# len(),min(),max(),index(),count() ----> all same as list

# to add element inside tuple ---> cannot add
# can not delete any element from tuple

t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)


# to add  all element inside list and tuple
sum()
l1 = (8,9,7,6)
print(sum(l1))



#* sort
t1 =(8,9,0,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=True)))



# * iterate list and tuples

# * iterate based on elements
l1 = [9,8,0,6,5]
for i in l1:
    print(i)
'''

# * iterate based on index value
l1 = [9,8,0,6,5]
for i in range (0,len(l1)):
    print(l1,i)

#print(l1[2])




























































































