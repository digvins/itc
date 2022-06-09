print("QUESTION 1")
print()
# Python program to convert Decimal to Binary Number
 
# input number
number = int(input("ENTER A NUMBER : "))
 
# binary output
# using the inbuilt function
print("the binary number is :", bin(number)[2::])

print()
print("QUESTION 2")
print()

num1=float(input("Enter a number : "))   # asking user to enter a number 
operation=input("Enter an Operation : ") # asking user tto enter an operation
num2=float(input("Enter another number : "))    # asking user to enter another number

if(operation=='+'):
    print("Your answer is ",num1+num2)
elif(operation=='-'):
    print("Your answer is ",num1-num2)
elif(operation=='*'):
    print("Your answer is ",num1*num2)
elif(operation=='/'):
    print("Your answer is ",num1/num2)
else:
    print("Invalid Input")

print()
print("QUESTION 3")
print()

#question 3(a.)
#   (3+4)*5

#question 3(b.)
#   n*(n-1)/2

#question 3(c.)
#   4*math.pi*r**2

#question 3(d.)
#   math.sqrt(r*(math.cos(a))**2+r*(math.sin(a))**2)

#question 3(e.)
#   (y2-y1)/(x2-x1)

print()
print("QUESTION 4")
print()

for i in range(5):
    print(i, end=" ")
print()
 
for i in range(3, 10):
    print(i, end=" ")
print()
 
for i in range(4, 13, 3):
    print(i, end=" ")
print()

for i in range(15, 5, -2):
    print(i, end=" ")
print()

for i in range(5, 3):
    print(i, end=" ")
print()

print()
print("QUESTION 5")
print()
carbon=int(input("Enter Number of Carbon Atoms -> "))
hydrogen=int(input("Enter Number of Hydrogen Atoms -> "))
oxygen=int(input("Enter Number of Oxygen Atoms -> "))

print("The Molecular weight of the compound is -> ",hydrogen*1.00794+carbon*12.0107+oxygen*15.9994)
