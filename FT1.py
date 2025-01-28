# import math
# x = 2.7
# y = -2.7
#
# print(math.ceil(y))
# print(math.floor(y))
#
# print(math.ceil(x))
# print(math.floor(x))

# CONDITIONAL STATEMENT

# good_credit = True
# price = 1000000
#
# if good_credit:
#     print("You have Good credit")
#     print("You got pay 10% of the price, which amount to: $" + str(0.1 *price))
# else:
#     print("You don't have Good credit")
#     print("You got pay 20% of the price, which amount to: $" + str(0.2 *price))
#
# print('Have a lovely day')

# AND OR AND NOT

# good_saving = True
# employed = False
#
# if good_saving and not employed:
#     print('He can be loaned from our bank')
# else:
#     print('He cannot be loaned')

#COMPARING OPERATIONS

# name = input("Enter your name: ")
#
# if len(name) < 3:
#     print("Your name must be at least 3 characters long")
# elif len(name) > 50 :
#     print("Your name must be at most 50 characters long")
# else:
#     print("Your name looks good")


## PROJECT ON WEIGHT
weight = float(input("Enter your weight: "))
unit =  input("unit of convertion (Kg or Lb): ")
new_unit = unit.lower()

if new_unit == 'lb':
    new_weight = 0.453592 * weight
    print("Your weight is " + str(new_weight) + " kg")
elif new_unit == 'kg':
    new_weight = 2.20462 * weight
    print("Your weight is " + str(new_weight) + " lb")
else:
    print("Invalid unit")
