''' Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9] '''
# accept the input as list of lists separated by space
l =list( map(list,input().strip().split()))
max =0
max_l =[]
print(l)
# function that takes the list as input and returns the sum of the elements
def sum_f (lol):
    sum=0
    for i in range(0,len(lol)):

        sum =sum+int(lol[i])
    return sum

for i in l:
    l_total =sum_f(i)
    if l_total > max:
        max = l_total # highest total
        max_l = i   # remember the list with highest total
# print the list as a list of integers
print(list(map(int,max_l)))