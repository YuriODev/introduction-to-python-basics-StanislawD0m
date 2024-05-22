# Exercise 6
# Your solution comes here
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("YES" * (a % b == 0) + "NO" * (a % b != 0))