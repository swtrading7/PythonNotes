# Input = Function that prompts the user to enter data
# Return the entered data as a String


name = input("What's your name?")
age = input("How old are you?")

age = int(age)
age = age + 1

print(f"Hello!{name}")
print("Happy Birthday!!!")
print(f"You are {age}")


# to make the whole code look better we can convert the data type to an integer from the begginnig

name = input("What is your name?")
name = int(input("How old are you?"))

age = age + 1

print(f"Hello!{name}")
print("Happy Birthday!!!")
print(f"You are {age}")


#Exercise: Calculate the Area of the Rectangle

length = float(input("Enter the Length"))
width = float(input("Enter the Width"))
area = length * width

print(f"The are is: {area}cm^2")

#Exercise: Shopping Cart

item = input("What item are you buying?")
price = float(input("What is the price?: "))
quantity = float(input("How many would you like?: "))
total_price = price * quantity

print(f"You have bought {quantity} of {item}/s")
print(f"Your Total Price is {total_price}€")
