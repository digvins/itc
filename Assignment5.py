#21102075
#DIGVIJAY SINGH RATHORE

print("QUESTION 1")
print("\n")

def reverse(line):
    line = "".join(reversed(line))
    return line
 
s = input("Enter a string : ")
 
print ("The original string is : ",end=" ")
print (s)
 
print ("The reversed string is : ",end=" ")
print (reverse(s))



print("\n")
print("QUESTION 2")
print("\n")
lwr=int(input("Enter lower range limit: "))    
upr=int(input("Enter upper range limit: "))
n=int(input("Enter the number to be divided by: "))
for i in range(lwr,upr+1):     #Using a for loop, print all the factors which is divisible by the number
    if(i%n==0):
        print(i)    # Whenever the remainder of the number divided by i is equal to 0, i is printed


print("\n")
print("QUESTION 3")
print("\n")
import math
def heronformula(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area                                                 # defined a function and written the heron's formula


side1=int(input("Enter first side: "))
side2=int(input("Enter second side: "))
side3=int(input("Enter third side: "))                          # Take in all the three sides of the triangle and store it in three separate variables

if side1+side2>side3 and side1+side3>side2 and side2+side3>side1 :
    htl=heronformula(side1,side2,side3)                             # stored the value of area in a variable htl
    print("Area of the triangle is: ",round(htl,2))                 # printed the output rounded upto 2 decimal figures 
else :
    print("Invalid Input")                                          # invalid input shown up if the triangle is not possible

print("\n")
print("QUESTION 4")
print("\n")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):                          # outer loop decides the row
        print("*", end=' ')                            # inner loop decides the column
    print("\r")                                        # used to keep space between stars

for i in range(rows, 0, -1):                           
    for j in range(0, i - 1):                          
        print("*", end=' ')
    print("\r")

print("\n")
print("QUESTION 5")
print("\n")
row=int(input("Enter the number of rows : "))
n=0

for i in range(0,row+1):
      
      for j in range(i): 
            if n==26:
                n=0 
            else:
                pass
            y=chr(65+n) 
            print(y, end="")
            n+=1
      print("")


print("\n")
print("QUESTION 6")
print("\n")
lower_value = int(input("Enter the Lowest Range Value : "))  
upper_value = int(input("Enter the Upper Range Value : "))    # input from user the lowest and the upper range
  
print ("The Prime Numbers in this range are : ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):                           # Check for each number if it has any factor between 1 and itself
            if (number % i) == 0:                             # if YES, the code will move on
                break       
        else:  
            print (number)                                    # if NO, the code prints the number

print("\n")
print("QUESTION 7")
print("\n")
lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)

print("\n")
print("QUESTION 8")
print("\n")
from collections import Counter

def count_occurrence(list, n):
    #counter variable
    count=0
    for i in list:
        if(i==n):
          #update counter variable
            count=count+1
    return count

  
# input of list
li=[]
n=int(input("Enter size of list : "))
for i in range(0,n):
    e=int(input("Enter element of list : "))
    li.append(e)

print("\n")
print("Answer of (a.) part")
print("Positive numbers in",li,"are : ")
  #traversing
for i in li:
      
    # checking condition
    if i>=0:
       print(i, end = " ")

print()
print("\n")
print("Answer of (b.) part")
print("negative numbers in",li,"are: ")
  #traversing
for i in li:
      
    # checking condition
    if i<0:
       print(i, end = " ")

print()
print("\n")
print("Answer of (c.) part")
print("odd numbers in",li,"are: ")
#traversing
for i in li:
      
    # checking condition
    if i%2!=0:
       print(i, end = " ")


print()
print("\n")
print("Answer of (d.) part")
print("even numbers in",li,"are: ")
  #traversing
for i in li:
      
    # checking condition
    if i%2==0:
       print(i, end = " ")

print()
print("\n")
print("Answer of (e.) part")
duplicate_li = Counter(li)

print(duplicate_li)           #to get occurence of each of the element.

print("\n")
print("QUESTION 9")
print("\n")
from collections import Counter
# input of list
li=[]
n=int(input("Enter size of list : "))
for i in range(0,n):
    e=int(input("Enter element of list : "))
    li.append(e)

duplicate_dict = Counter(li)

print(duplicate_dict)           #to get occurence of each of the element.
