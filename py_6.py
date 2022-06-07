# print the difference between two lists
# Accept the two lists of integers
l1 = list(map(int,input().strip().split()))
l2 = list(map(int,input().strip().split()))
l = list(set(l1)-set(l2)) +list(set(l2)-set(l1))
print(l)

