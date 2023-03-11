# check if a string is a palindrome

# malayalam, banana

string = input("Enter a string: ")

if string == string[::-1]:
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')