# check if a number is with in range

num = int(input('Enter a number: '))

if num in range(1,11):
    print(num, 'is between 1 and 10.')
else:
    print(num, 'is not between 1 and 10.')