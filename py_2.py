''' Write a Python program which accepts a sequence of comma-separated numbers from user and
generate a list and a tuple with those number '''
# comma separated input
x = input().split(sep=',')
# list
list_l= x
print(list_l)
tuple_t = (*list_l,) # converts list_l iterable to a tuple
print(tuple_t)
