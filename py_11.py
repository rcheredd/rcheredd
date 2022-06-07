"""  Write a Python program to multiply all the items in a dictionary  """


dic={1:10, 2:20,3:8}
total =1

for i in dic:
    total = total * dic[i]
print(total)
