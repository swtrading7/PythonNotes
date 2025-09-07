# Weight Conversion

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "Kilograms" or "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight,2)}{unit}: ")
if unit == "Pounds" or "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 2)}{unit}: ")
else:
    print(f"{unit} is not a valid unit")
