'''  Write a Python program to test whether a number is within 100 of 1000 or 2000. '''
n = int(input("Enter a number: "))
if abs( 1000 - n ) <= 100:
    print(f"Entered number {n} is with in 100 of 1000")
elif abs(2000 - n) <= 100:
    print(f"Entered number {n} is with in 100 of 2000")
else:
    print(f"entered number {n} is not within 100 of either 1000 or 2000")