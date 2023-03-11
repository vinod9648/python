# check if a password is valid based on its length

password = input('Enter your password: ')

if len(password) >= 8:
    print('Password is valid.')
else:
    print('Password is too short.')