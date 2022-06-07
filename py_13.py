"""  Write a Python program to convert a tuple to a dictionary.  """
# define the set with few values
tuple_t = (('red','R'), ('green','G'), ('blue','B'), ('white','W'), ('black','B'), ('orange','O'))

# Create a dictionary based on tuple of tuples using dict method
print(tuple_t)
dict_d = dict((y, x) for x, y in tuple_t)

print(dict_d)
