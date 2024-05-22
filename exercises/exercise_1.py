# Exercise 1
# Your solution comes here
five_digit = input("Enter a 5 digit number: ")
num1 = int(five_digit[0])
num2 = int(five_digit[1])
num3 = int(five_digit[2])
num4 = int(five_digit[3])
num5 = int(five_digit[4])
digit1 = str(num1 + num3 + num5)
digit2 = str(num2 + num4)
new_num = digit1 + digit2
print(new_num)