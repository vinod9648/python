# check if a number is multiple of another number

num = int(input('Enter a number: '))
divisor = int(input('Enter a divisor: '))

if num % divisor == 0:
    print(num, 'is a multiple of', divisor)
else:
    print(num, 'is not a multiple of', divisor)