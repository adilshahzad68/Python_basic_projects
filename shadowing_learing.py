# name = input('enter name: ')
# age = int(input('enter age: '))
# marks = float(input('enter marks; '))

# print('welcom', name)
# print('age=', age)
# print('marks=', marks)
# ============================

# Write a Program to input 2 numbers & print their sum

# num1 = int(input('Please enter first number:'))
# num2 = int(input('please enter 2nd number:'))
# sum = num1 + num2
# print('sum: ', sum)

# ============================================

# write a program to input side of a square and print its area.

# side = float(input('Enter square side:'))

# print('Area= ', side*side)

# =================================================

# write a program to input 2 floating point numbers and print their average.

# num1 = float(input('Enter first number:'))
# num2 = float(input('Enter second number:'))

# Avg = ((num1+num2)/2)

# print('Average = ', Avg)

# ==================================================

# # write to input 2 int numbers, a and b.
# # Print True if a is greater than or equal to b. if not print False.

# a = int(input('Please number for a: '))
# b = int(input('Please enter number for b: '))

# if (a >= b):
#     print('True')
# else:
#     print('False')

# ----------------or--------------------------------

# a = int(input('Enter first : '))
# b = int(input('Enter second : '))

# print(a >= b)
# ========================================

# index
# str = 'Adil Shahzad'

# print(str[3])
# ==========================================


# # slicing
# str = "Adil Shahzad"
# print(str[1:4])
# -========================================

# strl = "Adil Shahzad"
# print(len(strl))
# ======================================


# str = "My name is Adil Shahzad"
# print(str.endswith("zad"))
# ========================================

# str = "my name is adil"
# print(str.capitalize())
##############################################

# str = "My name is adil shahzad"
# print(str.replace("adil", "ali"))
# ============================================

# str = "My name is adil shahzad"
# print(str. find("a"))

# ===========================================

# str = "my name is adil shahzad"

# print(str.count("a"))
# =============================================

# write a program to input user first name and print its length.
# name = input("write you name: ")

# print("name digits are:  ", len(name))
# ==================================================

# wap to find the occurrence of 'S' in a string.

# str = "Hi, $I am $the $ symbol $666.66"
# print(str.count("$"))
# ====================================================

# conditional statements
# # if. elif. else (syntax)
# if (condition):
#     statement1
# elif (condition):
#     statement2
# else:
#     statementN
# ====================================================

# light = "red"

# if (light == "red"):
#     print("stop")
# elif (light == "green"):
#     print("go")
# elif (light == "yellow"):
#     print("look")
# else:
#     print("light is broken")
# print("End of code")

# -=================================================

# marks = int(input("please enter your marks: "))

# if (marks >= 90):
#     grade = "A"
# elif (marks >= 80 and marks < 90):
#     grade = "B"
# elif (marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of the student: ", grade)
# ==============================================

# write a program to check if a number entered by the user is odd or even?

# num = int(input("Please enter your number: "))

# result = num % 2

# if (result == 0):
#     print('Your number is EVEN')
# else:
#     print('Your number ODD')

# ====================================================

# write a program to find the greates of 3 numbers enterd by the user.

# a = int(input('Enter first number: '))
# b = int(input('Enter first number: '))
# c = int(input('Enter first number: '))

# if (a >= b and a >= c):
#     print('First number is largest', a)
# elif (b >= c):
#     print("Second number is largest", b)
# else:
#     print("Third number is largest ", c)

# ----------------------------------------------------------

# write a program to check if a number is a multiple of 7 or not?

# num = int(input("Please enter your number: "))

# if (num % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")

# ----------------------------------------------------------------------

# List

# marks = [55.5, 65.4, 63.2, 77.4, 97.2, 45.7]
# print(marks)
# print(type(marks))

# print(marks[1])
# print(marks[3])
# print(len(marks))
# -----------------------------------------------------

# student = ["Adil", 33.3, 23, 'Islamabad']
# print(student)

# ------------------------------------------------------------
# slicing

# marks = [55, 65, 54, 76, 32]
# print(marks[1:5])
# -------------------------------------------------------

# write a program to ask the user to enter names of their 3 favorite movies and store them in a list

# movies = []
# mov1 = (input("Enter 1st movie name: "))
# mov2 = (input("Enter 2nd movie name: "))
# mov3 = (input("Enter 3rd movie name: "))

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)
# ------------------------------------------------------------

# wap to check if a list contains a palidrome of elements. (hint: use copy() method)
# palidrome from last or from start read same like(maam), [1,2,3,2,1]

# list1 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if (copy_list1 == list1):
#     print("List is palindrome")
# else:
#     print("Not a palindrome")
# ---------------------------------------------------------

# wap to count the number of students with "A" grade in the fol tuple.

# ['C','D','A','A','B','B','A']

# grade = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
# print(grade.count('A'))

# -----------------------------------------------------

# store the aboe values in a list and sort them from A to D.

# grade = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
# grade.sort()
# print(grade)
# -----------------------------------------------------

# Dictionary in Python

# dict = {
#     "Key": "value",
#     "name": "Adil Shahzad",
#     "Subject": ["Math", "Physics", "Biology"],
#     "topic": ("dict", "sets"),
#     "Learning": "Python coding",
#     "age": 33,
#     "is_adult": True,
#     "Marks": 95.4
# }

# print(dict)

# ------------------------------------------------------------------

# nested dictionary

# student = {
#     "name": "Adil",
#     "subjects": {
#         "phy": 99,
#         "Math": 94,
#         "Bio": 88
#     }
# }

# print(student)

# -----------------------------------------------------------

# Set  (no duplicat in sets) empty set set() if we write set{} it will be dictionary.

# set = {1, 2, 3, 4, 4, 5, 6, "Adil", "Adil", "World"}
# print(set)
# print(len(set))  # total number of items

# ---------------------------------------------------------------

# store fol word meanings in a python dictionary:
# table: "a peice of furniture" , "list of facts and figures"
# cat: "a small animal"

# dict = {
#     "table": ["a piece of furniture", "list of facts and figures"],
#     "cat": "a small animal"
# }

# print(dict)
# ----------------------------------------------------------------------------
# sets
# you are given a list of subjects for students. Assume one classroom is required for 1
# subjet. How many classrooms are needed by all students.

# "python","java", "C++", "python", "javascript",
# "java","python","java", "C++","C"

# subjects = {
#     "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
# }

# print(subjects)
# -------------------------------------------------------

# marks = {}

# x = int(input("enter phy : "))
# marks.update({"phy": x})

# x = int(input("enter math : "))
# marks.update({"math": x})

# x = int(input("enter chem : "))
# marks.update({"chem": x})

# print(marks)
# ----------------------------------------------------------

# values = {9, "9.0"}
# print(values)

# ----------------------------------------------------

# while loop
# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1

# print(count)
# -----------------------------------------------------

# print numbers from 1 to 100

# i = 1

# while i <= 100:
#     print(i)
#     i += 1
# ------------------------------------------------------

# break

# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i += 1
# ------------------------------------------------------


# countinoue

# i = 0
# while i <= 5:
#     if (i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1
# ----------------------------------------------------

# print odd numbers from 1 to 10

# i = 1
# while i <= 10:
#     if (i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
# ----------------------------------------------------------

#  print even numbers from 1 to 10

# i = 1
# while i <= 10:
#     if (i % 2 != 0):
#         i += 1
#         continue

#     print(i)
#     i += 1
# -------------------------------------------------------

#  Foor Loop

# nums = [1, 2, 3, 4, 5]

# for val in nums:
#     print(val)

# -----------------------------------------------------

# str = "adilshahzad"

# for char in str:
#     print(char)
# else:
#     print("END")
# ---------------------------------------------------------

# print the element of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums:
#     print(el)

# --------------------------------------------------------------

# search for a number x in this tuple using loop

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49

# idx = 0
# for el in nums:
#     if (el == x):
#         print("number found at idx", idx)
#     idx += 1
# ===========================================================

# range

# print(range(5))
# ---------------------------------------------------------------

# seq = range(5)
# for i in seq:
#     print(i)
# --------------------------


# for i in range(10):   # range(stop)
#     print(i)

# for i in range(2,10):  # range(start, stop)
#     print(i)

# for i in range(2, 10, 2):  # range(start, stop, step)
#     print(i)
# ===================================

# for i in range(2, 100, 2):
#     print(i)

# ------------------------------------

# Practic


# using for and range()
# print numbers from 1 to 100.
# for i in range(1, 101):
#     print(i)
# -------------------------------------------

# print numbers from 100 to 1
# for i in range(101, 0, -1):
#     print(i)
# ----------------------------------------

# print the multiplication table of a number n

# n = int(input("enter number : "))

# for i in range(1, 11):
#     print(n * i)

# ------------------------------------------------

# wap to find the sum of first n numbers (using whileloop)

# n = 6
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("Total sum is", sum)

# --------------------------------------------------------------------------
# wap to find the factorial of first n numbers. (using for)

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("Total factorial = ", fact)
# -------------------------------------------------


# --------       Functions-------------------
# parameters input values like a and b , and argument pass values from parameters.
# def calc_sum(a, b):
#     sum = a+b
#     print(sum)
#     return sum


# calc_sum(5, 10)
# # more lines of code

# calc_sum(12, 14)


# # more line of code , again call the function

# calc_sum(15, 15)

# ---------------------------------------------------------
# function definition
# def calc_sum(a, b):  # parameters
#     return a+b


# sum = calc_sum(22, 40)  # funciton call, arguments
# print(sum)
# ---------------------------------------------------------

# def print_hello():
#     print("Hello Adil")


# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# =====================================================

# average of 3 numbers
# def calc_avg(a, b, c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg


# calc_avg(1, 2, 3)
# calc_avg(98, 97, 95)
# ------------------------------------------------------

# Practice of functions

# waf to print the length of a list (list is the parameter)
# cities = ["Karachi", "Lahore", "Islamabad", "Jhang", "Rawalpindi", "Attock"]
# heroes = ["Adil", "Ali", "Nomi", "Ahmed", "Fadi"]


# def print_len(list):
#     print(len(list))


# print_len(cities)
# print_len(heroes)
# --------------------------------------------------------------------

# waf to print the elements of a list in a single line. (list is the parameter)
# cities = ["Karachi", "Lahore", "Islamabad", "Jhang", "Rawalpindi", "Attock"]
# heroes = ["Adil", "Ali", "Nomi", "Ahmed", "Fadi"]


# def print_len(list):
#     print(len(list))


# def print_list(list):
#     for item in list:
#         print(item, end=" ")


# print_list(cities)
# print_list(heroes)
# ------------------------------------------------------------

#  waf to find the factorial of n (n is th parameter)

# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

# ------------------  or --------------------

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)


# cal_fact(6)

# ----------------------------------------------

# write a function to convert USD to Pkr.

# def converter(uds_val):
#     pkr_val = uds_val * 270
#     print(uds_val, "USD =", pkr_val)


# converter(1)

# -------------------------------------

# ----- Recursion---------------------

# when a function calls itself repeatedly.

# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)


# show(5)  # 5,    4=n-1,  3=n-2,  2=n-3,  1

# ------------------------------------------------------
#   Recursion

# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n


# print(fact(4))

# -----------------------------------------------------------

# write a recursive function to calculate the sum of first n natural numbers.

# def calc_sum(n):
#     if (n == 0):
#         return 0
#     return calc_sum(n-1) + n


# sum = calc_sum(10)
# print(sum)

# ------------------------------------------------------------

# write a recursive function to print all elements in a list.

# def print_list(list, idx=0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)


# fruits = ["mango", "litchi", "apple", "banana"]

# print_list(fruits)
# ----------------------------------------------------------

# I/O python

# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()
# ----------------------------------------

# With syntax

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# ------------------------------------------------

# Deleting a File
# using the os module, Module(like a code library) is a file written by another programmer taht generallyhas a function we can use.

# import os
# os. remove("sample.txt")

# --------------------------------------------------

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O \n")
#     f.write("using Java.\nI like programming in Java.")

# -----------------------------------------------------

# replace text Java with pyton in the file.

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)


# with open("practice.txt", "w") as f:
#     f.write(new_data)

# -------------------------------------------------------


# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r")as f:
#         data = f.read()
#         if (data.find(word)) != -1:
#             print("Found")
#         else:
#             print("not found")


# check_for_word()

# -----------------------------------------------------------

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1


# print(check_for_line())
# ---------------------------------------------------------------

# ---------OOPs-----------------

# class and object

# class Student():
#     name = "Adil"


# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)
# ===============================================
# another example

# class Car:                   #classs
#     color = "blue"
#     brand = "BMW"


# car1 = Car()                 # object
# print(car1.color)
# print(car1.brand)
# ------------------------------------------------

#    _init_ Function
#   Constructor
# All classes have a function called _init_(), which is always executed when the object is being initated.


# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Databas..")


# s1 = Student("Adil", 98)
# print(s1.name, s1.marks)      # Adil

# s2 = Student("Kamran", 90)
# print(s2.name, s2.marks)
# -------------------------------------------------------------

# ------------Class and Instance Attributes(data)

# Class.attr
# obj.attr

# --------------------------------------

# class Student:        # class
#     college_name = "ABC College"      # class attributes

#     # self by defult, name and marks parameters  # constructor (use of object initalization)(use to create new attributs)
#     def __init__(self, name, marks):   # self use of objects
#         self.name = name             # object attributes
#         self.marks = marks

#     def welcome(self):  # fuction or methos
#         print("welcome student,", self.name)

#     def get_marks(self):  # fuction or methos
#         return self.marks


# s1 = Student("Adil", 97)    # object
# s1.welcome()
# print(s1.get_marks())


# -----------------------------------------------------

# Practice
#  create student class that takes name and marks of 3 subjects as arguments in constructor
#  then create a method to print the average

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is: ", sum/3)


# s1 = Student("Adil Shahzad", [99, 98, 97])
# s1.get_avg()

# -------------------------------------------------------

# --------- Static Methods---------

# Methods that donot use self parameters (work at class lever)
# class Student:
#  @staticmethod  # decorator
# def college():
#      print("ABC College")

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod  # decorator use of static method
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is: ", sum/3)


# s1 = Student("Adil Shahzad", [99, 98, 97])
# s1.get_avg()
# s1.hello()

# ------------------------------------------------------

# very important---------

# 1. Abstraction
# Hiding the implementation details of a class and only showing the essential feature to the user

# 2. Encapsulation
#    Wrapping data and functions into a single unit (object).


# Abstraction

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started....")


# car1 = Car()
# car1.start()

# ----------------------------------------------------

# Practice

# Create bank account class with 2 attributes - balance and account number.
# Create methods for debit, credit and printing the balance.


# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs. ", amount, "was debited")
#         print("Total balance = ", self.get_balance())
#     # debit method

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs. ", amount, "was credited")
#         print("Total balance = ", self.get_balance())

#     # function for balance
#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000, 1234567)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# -------------------------------------------------

# del keyword
# used to delete object properties or object itself.
#  del s1.name
#  del s1

# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("Adil")
# print(s1.name)
# del s1.name
# print(s1.name)

# -----------------------------------------------------

# Private(like) attributes and methods
# conceptual implementations in Python
# Private attributes and methods are meant to be used only within the class and are not
# accessible from out side the class.
# ------------------------------------------------------------


# Inheritance
# When a class(child/derived) derives the properties and methods of another class(parent/base)


#   Single Inheritance

# class Car:
#     color = "black"

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")


# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name


# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.name)
# print(car1.start())
# print(car1.color)
# -------------------------------------------------------

# Multi- level Inheritance

# class Car:

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")


# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name


# class Fortuner(ToyotaCar):
#     def __init__(self, name):
#         self.type = type


# car1 = Fortuner("diesel")
# car1.start()

# ----------------------------------------------------------

# Multipule Inheritance

# class A:
#     varA = "welcome to class A"


# class B:
#     varB = "welcome to class B"


# class C(A, B):
#     varC = "welcome to class C"


# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# ------------------------------------------------------

# Super method
# super() method is used to access methods of the parent class.

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()


# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# --------------------------------------------------------

# Class method
#  A class method is bound to the class and receives the class as an implicit first argument

# Note: static method can't access or modify class state and generally for utility.
#   class Student:
#       @ classmethod   #decorator
#       def college(cls):
#           pass

# example

# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1. changeName("Adil Shahzad")
# print(p1.name)
# print(Person.name)

# ------------------------------------

# Property decorator.
# we use @property decorator on any method i nthe class to use the method as a property.
# example
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"


# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)
# ------------------------------------------------------------

# Polymorphism : Operator Overloading
# when the same operator is allowed to have differnt meaning according to the context
# operators and Dunder functions
# a + b    a.__add__ (b)
# a-b      a.__sub__(b)
# a*b      a.__mul____(b)
# a/b      a. __truediv____(b)
# a%b      a. __mod____(b)

# ====================================

# example
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)


# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()
# -------------------------------------------------------------


# Let's Practice

# Qs. Define a Circle class to create a circle with radius r using the constructor.

# Define an Area() method of the class which calculates the area of the circle.

# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7) * self.radius


# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


# ----------------------------------------------------------
# Qs. Define a Employee class with attributes role, department & salary. This class also

# showDetails() method.

# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self. role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)


# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")


# engg1 = Engineer("Adil Shahzad", 40)
# engg1.showDetails()
# -----------------------------------------------

# Example
# Q: Create a class called Order which stores item and its price.
#   Use Dunder function __gt__() to convey that:
#       order1>order2 if price of order1 > price of order2

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price > odr2.price


# odr1 = Order("chips", 20)
# odr2 = Order("tea", 15)

# print(odr1 > odr2)  # True

# =-----------------------------------------------------
