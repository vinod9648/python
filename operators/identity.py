# is
a = [1, 2, 3]
b = [1, 2, 3]
if a is b:
    print("a and b refer to the same object")
else:
    print("a and b do not refer to the same object")   # Output: a and b do not refer to the same object

# is not
a = [1, 2, 3]
b = [1, 2, 3]
if a is not b:
    print("a and b do not refer to the same object")
else:
    print("a and b refer to the same object")   # Output: a and b do not refer to the same object
