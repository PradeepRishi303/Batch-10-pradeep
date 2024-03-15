'''
 # -----> while loop
 # -----> break using while loop

 # eg;1
 # 1.) iterate from 20 to 30 and break the loop in 27

#i = 20
#while i<31:
#    if i ==27:
#       break
#    print(i)
#   i+=1


# 2.)
#i = 20
#while i<31:
#    print(i)
#   i+=1
#
#    if i==27:
#        break

# 3.)
#i = 20
#while i<31:
#    print(i)
#    if i==27:
#        break
#   i+=1

#4.)
# = 20
#while i<31:
#    if i==27:
#        print(i)
#       break:
#    i+=1

# -------> continue

# ----> Eg:1
#i = 20
#while i<31:
#    if i==27:
#       continue
#    print(i)
#    i=i+1

# Eg.2
#i = 20
#while i<31:
#    i=i+1
#    if i==27:
#        continue
#   print(i)

# ! Eg:3
# while to lterate from 12 to 22
# find the sum of all numbers

#i = 12
#sum=0
#while i<22+1:
#     sum=sum+i
#     print(sum)
#    i+=1

# Eg:6
# find the avreage of value from 20 to 30
#i = 20
#sum=0
#count = 0
#while i<30:
#     sum=sum+i
#     count+=1
#     i+=1
#print(sum/count


 ------> nested for loop
 # Eg :1

for row in range(1,3+1):
     for col in range(1,4+1):
         print(row,col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()



print(1, end=" ")
print(2)
print(3)
print(4)



sum = 0

for row in range(5):
    for col in range(5):
        sum= sum+1
        print(row, end=" ")
    print()



# ! to print stars in right angled triangle

for row in range(0, 6):
    for col in range(0, row+1):
        print("*", end=" ")
    print()


# eg:2
for row in range(0,9):
    for col in range(0,row+1):
        print("$", end=" ")
    print()


#* * * * *
#* * * *
#* * *
#* *
#*

for row in range(0,6):
    for col in range(row,6):
        print("*", end=" ")
    print()



for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()







for row in range(0,5):
    for col in range(0,6):
        if((row==o and col==3) or (row==1 and(col>=2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

        


for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()







for row in range(0,6):
    for col in range(0,6):
        if(col
            print("*",end=" ")
        else:
            print(" ", end=" ")
        print()




# ------> List

# ------>Data types

  # primary
      #string
      #Bollean
      #Set
      #Dictionary

  # Collection
     # List
     # Tuple
     # Set
     # Dictionary

# ? -------> List
# 1.) if the collection elements are surrounded by square brackets, it is considered
# to be list
# ! eg:
     #l1=[4,7,9,89,"hello",7+9j, [8,9,0]]
# characteristics of list:
# 1.) list have to be sorrounded by []
# 2.) It is mutable (the element in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The element inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# To access the elements in list
l1 = [1, 4, 1, 7,89.7,75, "p", "i"]
# print(l1)

# ----> Indexing
#In the collectiondata types like list, tuple, string, the elements will be alloted
# with predefines unique value called index value

# we have 2 types of indexing
# Positive indexing --> starts with 0 from left hand side
# Pegative indexing --> strats with -1 from right hand side


# Positive indexing
lst1 = [1, 4, 1, 7,89.7,7.5, "p","i"]

print(lst1[0])
print(lst1[4])
print(lst1[20])


# ? -----> Negative indexing
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-1])
print(lst1[-5])

 

# ? ----> slicing
# lst1[start_index:end_index:step]
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[0:8])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])


print(lst1[0:7:1]) # lst1[0:7] ---> both are same
pruint(lst1[0:7:2])



# trail = int(input())


lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-4:-1])
#print(lst1[-1:4]) --->[]
print(lst1[-7:-1])
print(lst1[-7:-1:2])



# ! To interest ot add element inside list
'''

# append() ---> used to add element at last position of list
l1 = [9,8,0,6]
l1.append("car")
print(l1)










































                 

            
         





 
