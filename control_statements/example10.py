# check if a list contain certain element

my_list = [1, 2, 3, 4, 5]

search_element = int(input('Enter a number to search for: '))

if search_element in my_list:
    print('The list contains', search_element)
else:
    print('The list does not contains', search_element)