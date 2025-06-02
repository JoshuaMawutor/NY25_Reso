# for x in range(2,6):
#      for n in range(2,x):
#           if x % n == 0:
#                print({x} , '%' ,{n} , 'have no remainder = ', str(x%n))
#           else:
#                print({x} ,'%' , {n} , 'have remainder = ', str(x%n))

#
# total = 0
# i = 0
# while i <= 100:
#     total += i
#     i += 3
# print(total)
total = 0
num = 0

#
# def fraction(number):
#     if number/4 == 0:
#         return "That is quarter of the number"
#     elif number/2 == 0:
#         return "That is half of the number"
#     elif number/8 == 1:
#         return "That is 1/8th of the number"
#     else:
#         return "That is a whole number"
#
# print(fraction(7))

Cat_name = []
while True:
    print('The name of the cat :' + str(len(Cat_name) + 1))
    name = input()
    Cat_name = Cat_name + [name]
    if name == '':
        break

for cat in Cat_name:
    print(cat)