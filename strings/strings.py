# 1. Creating a string variable:
my_string = "Hello, world!"

# 2. Accessing characters in a string using indexing:
my_string = "Hello, world!"
print(my_string[0])  # Output: "H"
print(my_string[4])  # Output: "o"

# 3. Slicing a string to get a substring:
my_string = "Hello, world!"
print(my_string[0:5])  # Output: "Hello"
print(my_string[7:])   # Output: "world!"

# 4. Concatenating strings using the + operator:
string1 = "Hello"
string2 = "world"
my_string = string1 + ", " + string2 + "!"
print(my_string)  # Output: "Hello, world!"

# 5. Repeating a string using the * operator:
my_string = "Hello"
repeated_string = my_string * 3
print(repeated_string)  # Output: "HelloHelloHello"

# 6. Formatting strings using the format() method:
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))  # Output: "My name is Alice and I am 25 years old."

# 7. Using f-strings for string interpolation:
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: "My name is Alice and I am 25 years old."


# Looping Through a String
for x in "banana":
  print(x) 
# b
# a
# n
# a
# n
# a