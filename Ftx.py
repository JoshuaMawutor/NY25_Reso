# while True:
#     name = input('Enter your username: ')
#     name = name.capitalize()
#     if name !='Joshua':
#         print('Wrong username')
#         continue
#     print('Welcome', name)
#     print('Type your password', name.upper())
#     password = input('Enter your password: ')
#     if password == '<PASSWORD>':
#         print('you have successfully logged in')
#         break

birthday = {'Josh': 'Nov 16', 'Rich': 'April 22', 'Mike': 'Sept 8'}
while True:
    print('Enter the name for birthday info')
    name = input('enter name: ')
    if name == '':
        break

    if name in birthday:
        print(name + ' celebrate birthday on ' + birthday[name])
    else:
        print('We dont have a birthday details in our records')
        bday = input('enter bday: ')
        birthday[name] = bday
        print('Thanks! database have been updated')

    if len(birthday.keys()) >= 10:
        break

for nam, day in birthday.items():
    print(nam, day)

