# Variable = A container for value ( string, integer, flat, boolean )
# A variable behaves as if it was the VALUE it contains
# there are Strings ( Series of Characters "also can include numbers" )
first_name = "Stas"
food = "fruit"
print(f"Wassup {first_name}")
print(f"You like {food}")


#Integers | f"" servers as an intermedium, it's a string technically, but you can comment for the public
age = 18 #Shouldn't be in quotes "" because that would be considered a String 
quantity = 3
num_of_students = 25
print(f"you are {age} years old")
print(f"you like {food}")
print(f"your class has {num_of_students} students")


#Float ( Number that contains a decimal portion=
price = 10.99
gpa = 1.9
distance = 5.5


print(f"The price is {price}€")
print(f"The gpa is {gpa}")
print(f"The distance is {distance}km")

#Boolean |A boolean is either True or False

is_student = True

if is_student:
    print("You ARE a student")
else:
    print("You are NOT a student")


for_sale = False

if for_sale:
    print("Item available")
else:
    print("Item Unavailable")

is_online = True

if is_online:
    print("Online")
else:
    print("Offline")


#Exerciese | Video Game Registration Example
first_name = "Roger"
last_name = "theHoneyBadger"
age = 99
number_of_granddaughters = 2
years_to_birthday = 1.6
print(f"Your first name is {first_name}")
print(f"Your last name is {last_name}")

print(f"Your age is {age}")
print(f"Your number of granddaughters is {number_of_granddaughters}")
print(f"Time until your birthday is {years_to_birthday}")
are_alive = True
if are_alive:
    print("Congratulations! You are alive")
else:
    print("My deepest condolences")         
