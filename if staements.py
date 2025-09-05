# if = Writ code IF some condition is True
# else, so somthing else
age = int(input("How old are you?:"))
if age <= 18:
    print("You are signed!")
elif age < 0:
    print("Incorrect age")
elif age > 100:
    print("Incorrect age")
else:
    print("You are not signed!")
