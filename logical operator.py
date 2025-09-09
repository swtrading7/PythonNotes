#logical operators = evaluate multiple conditions (or, and, not )
    #or = at least one condition must be True
    #and = both conditions must be TRUE
    #not = inverts the condition ( not False, not True)

# temp = 25
# is_raining = false
#
# if temp > 35 or temp < 0 or is_raining:
#     print("Event is Cancelled")
# else:
#     print("Event ongoing")

# temp = 25
# is_sunny = True
#
# if temp >= 28 and is_sunny:
#     print("Go touch some grass")
#     print("It's sunny")
# elif temp <= 0 and is_sunny:
#     print("It's cold outside")
#     print("It's sunny")
# elif 28 > temp > 0 and is_sunny:
#     print("It's warm outside")
#     print("It's sunny")

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("Go touch some grass")
    print("It's sunny")
elif temp <= 0 and is_sunny:
    print("It's cold outside")
    print("It's sunny")
elif 28 > temp > 0 and is_sunny:
    print("It's warm outside")
    print("It's sunny")
elif temp <= 0 and not is_sunny:
    print("It's cold outside")
    print("It's sunny")
elif 28 > temp > 0 and not is_sunny:
    print("It's warm outside")
    print("It's sunny")
