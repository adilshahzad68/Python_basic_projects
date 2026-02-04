"""
temperature = 15
if temperature > 30:
    print("it is warm")
    print("Drink Water")
elif temperature > 20:
    print("Its nice")
else:
    print("Its cold")
print("Done")


age = 32
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

    # or

age = 32
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# or

age = 32

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# logica orperators and, or , not
# and

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
# and another example (both conditions should be true)

high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# or (only codition)

high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")


# not

high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not Eligible")

# all operator together

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# logical operaters are short cecuit mean if first condition false it not check other condition and its stopped

# age should be between 18 and 65

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# --------------or ------------

age = 22
if 18 <= age < 65:     # chaining comparison operators
    print("Eligible")

# ----------------------------------

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
# _________________________________________

# Loops  (for loop)

for number in range(3):
    print("Attempts", number + 1, (number + 1) * ".")
# or-----------------same-----

for number in range(1, 4):
    print("Attempts", number, number * ".")
# --------------------------------------

for number in range(1, 10, 2):
    print("Attempts", number, number * ".")

# -----------------------------------------------------

# for else

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# ....................................

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# --------------------------------------

# Nested Loop  (loop inside loop)

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
# ________________________________


# Iterable

for x in "Python":
    print(x)

# List

for x in [1, 2, 3, 4]:
    print(x)
# ____________________________

# While loop
number = 100
while number > 0:
    print(number)
    number //= 2
# .............................

command = ""
while command != "quit":
    command = input(">")
    print("Echo", command)
    break
    
# ///////////////////////////// run manually

# exercise
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")

# ////////////   print () and round () are function
# creat own custom function


def greet():
    print("Hi there")
    print("Welcome abroad")


greet()

# ...................


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome abroad")


greet("Mosh", "Hamedani")
greet("John", "Smith")
"""
# ---------------------------
# there are 2 types of functions
# 1 - Perform a task
# 2 - Return a value like round(1.9)


def increment(number, by=1):
    return number + by


print(increment(2, 5))
# ------------------------------------


def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)
# -------------------------------------


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
