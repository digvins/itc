# Question 1 
a=input("Enter first number")
b=input("Enter second number")
c=input("Enter third number")
d=(int(a)+int(b)+int(c))/3
print("The average of three numbers =")
print(float(d))



# Question 2 
standard_deduction=10000
dependent_deduction=3000
gross=input("Enter the gross income")
No_of_dependents=input("Enter the number of dependents")
taxable_income=int(gross)-int(standard_deduction)-(int(dependent_deduction)*int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :")
print(float(tax))



# Question 3
SID=input("Enter the SID")
Name=input("Enter the name")
Gender=input("Enter your Gender ")
Course_name=input("Enter the course name")
CGPA=float(input("Enter your CGPA"))
STUDENT=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT)



# Question 4

a=float(input('marks obtained by student 1:'))
b=float(input('marks obtained by student 2:'))
c=float(input('marks obtained by student 3:'))
d=float(input('marks obtained by student 4:'))
e=float(input('marks obtained by student 5:'))
marks_list=[a,b,c,d,e]
marks_list.sort()
print(marks_list)


# Question 5
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("Part a question : ",colour)
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple']
print("Part b of question :",colour) 
