# Exercise 8
# Your solution comes here
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
smallest = (n1 * (n1 < n2 and n1 < n3)) + (n2 * (n2 < n1 and n2 < n3)) + (n3 * (n3 < n2 and n3 < n1))

largest = (n1 * (n1 > n2 and n1 > n3)) + (n2 * (n2 > n1 and n2 > n3)) + (n3 * (n3 > n2 and n3 > n1))

print(smallest)
print(n1 + n2 + n3 - smallest - largest)
print(largest)
