while True:
    name = input('Enter your username: ')
    name = name.capitalize()
    if name !='Joshua':
        print('Wrong username')
        continue
    print('Welcome', name)
    print('Type your password', name.upper())
    password = input('Enter your password: ')
    if password == '<PASSWORD>':
        print('you have successfully logged in')
        break
