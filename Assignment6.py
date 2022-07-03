print("QUESTION 1")

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
pernum=int(input("Write a number : "))
print(perfect_number(pernum))

print('\n')
print("QUESTION 2")

def Palindrome(s):
    return s == s[::-1]                   # function which return reverse of a string
 
 

pal=input("Write a string to check if it's a Palindrome : ")

ans = Palindrome(pal)
 
if ans:
    print("Yes")
else:
    print("No")

print('\n')
print("QUESTION 3")

from math import factorial
 
# input n
n=int(input("Number of rows : "))
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    # for new line
    print()


print('\n')
print("QUESTION 4")

import string
  
def pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      

string = input("Write a string to check if it's a pangram : ")
if(pangram(string) == True):
    print("Yes")
else:
    print("No")



print('\n')
print("QUESTION 5")

n=input("Enter the string : ") 
l=n.split('-') 
l.sort() 
print('-'.join(l)) 

print('\n')
print("QUESTION 6")

class student_data:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch

    def student_id(self):
        print(f'name : {self.name} ||| branch : {self.branch}')

s=student_data('DIGVIJAY','CIVIL')
s.student_id()

print('-->',s.name)
print('-->',s.branch)

print('\n')
print("QUESTION 7")

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))


print('\n')
print("QUESTION 8")

def findTriplets(arr, n): 
  
    found = True
    for i in range(0, n-2): 
      
        for j in range(i+1, n-1): 
          
            for k in range(j+1, n): 
              
                if (arr[i] + arr[j] + arr[k] == 0): 
                    print(arr[i], arr[j], arr[k]) 
                    found = True
      
              
    # If no triplet with 0 sum  
    # found in array 
    if (found == False): 
        print(" not exist ") 
  

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr) 
findTriplets(arr, n)


print('\n')
print("QUESTION 9")

def checkBalance(str1):  
    count= 0  
    ans=False  
    for i in str1:  
        if i == "(" or i == "{" or i == "[":  
            count += 1  
        elif i == ")" or i == "}" or i == "]":  
            count-= 1  
        if count < 0:  
            return ans  
    if count==0:  
        return not ans  
    return ans  
str1=input("Enter a string of brackets: ")   
print("Given string is balanced :",checkBalance(str1))  
