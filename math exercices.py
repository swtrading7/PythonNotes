# Calculate the Circumfracne o the circle
import math

radius = float(input("Enter radius: "))

circumference = 2 * math.pi * radius

print(f"The Circumference of the circle with radius {radius} is: {round(circumference, 2)}cm")


#Calculate the Area of the Circle

radius = float(input("Enter radius: "))

area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {round(area), 2}")

#Hypotenuse

a = float(input("Enter a: "))
b = float(input("Enter b: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Hypotenuse is: {c}")
