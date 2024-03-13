# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not

#length = int(input())
#breadth = int(input())
#if length==breadth:
#    print("its a square")
#else:
#    print("its not a square")

# ! Eg:4
# Python program to chechk whether the
# given integer is a multiple of both 5 and 7

#n=int(input("enter the number: "))
#if n%5==0 and n%7==0:
#    print("yes")
#else:
#    print("no")


# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria :

#       cost price (in Rs)                                Tax
#       >100000                                            15 % + discount 6%
#       >50000 and < = 100000                              10%
#       <50000                                             5%


#price = int(input("enter the price"))
#amount = 0
#if price >=100000:
#   discount = price*(6/100)
#   value = price-discount
#   amount=value*(15/100)
#   total = value+tax
#else:
#    tax = price*(5/100)
#    total = price+tax
#print("The onroad cost of bike is: ",total)            
            
# if elif
# Eg: 1
#a=7
#b=9
#c=3

#if a >b and a<c:
#    print("A is greater")
#    print("B is greatrer")
#elif c>a and c>b:
#    print("C is greater")


#A school has following rules for grading system
# a.below 25 - F    
# b.25 to 45 - E
# c.45 to 50 - D
# d.50 to 60 - C
# e.60 to 80 - B
# f.above 80 - A
# Ask user to enter the marks and print the corresponding grade

#mark = int(input("enter the mark:"))
#if mark>=80 and mark<=100:
#    print("A")
#elif mark>=60 and mark<80:
#    print("B")
#elif mark>=50 and mark<60:
#    print("c")
#elif mark>=40 and mark<50:
#    print("D")
#else:
#     print("fail")

# ! --> short hand if else
#Eg:1
#a=9
#b=60
# if a>b:
#    print("A")
#else:
#      print("B")
#? ---> using short hand if else
# *Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.)   Always it have to end with else

# print("A") if a>b else print("B")


# ! code to check the givenn char is vowel or consonent
# char=input("enter the char: ")
# if char=="a" or char =='e' or char =='i' or char=='o' or char=='u':
#    print("is a vowel")
# else:
#    print("is a consonent")

# ? or

# str1 = "aeiouAEIOU"
# if char in str1:
#     print("vowel")
# else:
#   print("consonnt")

# ! shorthand if else
# char = input("enter the char:")
# str1 = "aeiouAEIOU"
# print("vowels") if char in str1 else print("consonent")

# !---> elif ladder using short hand if else
# Eg:1
# ? Find greatest among 3 variables using short hand if else
# a = 8
# b = 5
# c = 9

# print("A is greater") if a>b and b>c else print("B is greater")
# if b>a and b>c else print("c is greater")

# ! ----------> looping

# looping can be implemented
# for loop
# while loop
 
# ! ---> for loop
# ? for loop is used for iteartion, if we know the number of loop have to run
# ? it is used to iterate the iterables eg(string, list, tuple, etc..)

# todo ---> syntax for loop

# ! for syntax in c
# for(i=0;i<10;i++){
#     printf("hello");
# }

# ! for syntax in python
# for userdefined_variable in range(start, end, step): default setup value is 1
#   statement
#   statement
#   statement

# ? Eg:1
# To print the value from 1 to 10 using for loop

# for i in range(0, 10): #(n , n-1)
#     print(i)
#     print("hello")


# ? eg:2
# for val in range(1,15,2):
#    print(val)
# for val in range(34,99):
#    print(val)
# ? Eg:3
# to decrement the value

# for val in range(10, 0, -1):
#    print(val)
    
# for val in range(99,0,-22):
#    print(val)
     
# ? eg:4
# ! print the output of 7th multiplivation table from 21 to 43
# for val in range (21,43+1,7):
#    print(val)
#for val in range(1,24+6):
#        print('7','X', val,'=',val*7) 
#        ans="7X{}={}"
#        print(ans.format(val, val*7))

# ---> method:3
# print(f"7 X {val}={val*7}")


# ? eg:5
# break ----> is used teerminate the loop

# for val in range(1, 999):
#    if val ==999:
#        break
#   print(val)

# Eg:6
# for val in range (1,99):
#    print(val)
#    if val ==86:
#        break


# Eg:7
# for val in range(1,10):
#    if val ==6:
#        print(val)
#        break


# ! continue
# Eg:1
#for val in range(1,10):
#    if val ==9:
#       continue
#    print(val)

# ! practise problems
# ? print the even number between 20 to 40
#for val in range(20,40,2):
#    if val %2==0:
#     print(val)

#!--------> while loop
# while is used when we do not know the number of times the loop have to run
# ? to iterate the non iterable elements while loop is used

# todo syntax

# intialisation
# while condition
#      statement
#      incre or decre

#! eh:1
# to iterare number from 1 to 10

# i = 10
# while i<11:
#    print(i)
#   i=i+1 # or I+=1

# eg:2
# to decrement using while loop
i=10
while i>0:
    print(i)
    i-=1
        

# for loop practise
# write a program to display sum of odd numbers and even
# numbers that fall between
# 12 and 37(including both numbers)


# ! ----> 1-4+9-16+25=15
n = int(input("enter number:"))
sum=0
for val in range(1, n+1):
    sq=val*val
    if val %2!=0:
        sum=sum+sq
    else:
        sum=sum-sq
    print(sum)


#assignment
# 1.) cats and mouse :kacker rank
# 2.) print the factorial of 8 using for loop
# 3.) write a program to display sum of odd numbers and even
# number that fall between
# 12 and 37 (including both numbers)
# 4.) write code to print the sum  of number using wgile loop
# n1  = 123 --> 1+2+3 = 6





                 







 
        
