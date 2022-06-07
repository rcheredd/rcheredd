"""Write a Python program to remove specific words from a given list.
Original list:
['red', 'green', 'blue', 'white', 'black', 'orange']
Remove words:
['white', 'orange']"""

orig_l = ['red', 'green', 'blue', 'white', 'black', 'orange']
new_l =[]
orig_l.remove('white')
orig_l.remove('orange')
print(orig_l)