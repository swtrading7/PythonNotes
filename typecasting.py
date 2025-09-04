#Typecasting =  converting the variable data type to another
# str() ; int() ; float() ; bool()

name = "sw"
age = 18
gpa = 3.9
is_student = True


#Conversion from one data type to another

age = str(age)
age += 1
print(type(age))


#The above is incorrect due to the fact that the data of the integer we converted to a String is now considered a String itself and wont be able to conect with another intager.
# But if we instead do like this:

age = str(age)
age += "1"
print(type(age))

# It's now able to read, since an integer ( age ) was converted to a String ( Data with value of a Word ), we have converted the 1 from being an integer into a string, making them from the same family again.
