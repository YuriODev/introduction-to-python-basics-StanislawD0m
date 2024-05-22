# Exercise 11
# Your solution comes here
s = int(input("Enter the total costs of the products purchased: "))
five_hund_dollar = s // 500
five_dollar = (((s % 500) % 100) % 10) // 5
one_hund_dollar = (s % 500) // 100
ten_dollar = ((s % 500) % 100) // 10
one_dollar = (((s % 500) % 100) % 10) % 5
print(f"{five_hund_dollar} (500),{one_hund_dollar} (100),{ten_dollar} (10),{five_dollar} (5),{one_dollar} (1)")