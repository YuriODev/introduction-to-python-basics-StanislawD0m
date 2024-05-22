# Exercise 3
# Your solution comes here
n = int(input("How many seconds have passed from the beginning of the day? "))
hours = n // 3600
minutes = (n % 3600) // 60
seconds = (n % 3600) % 60
while hours > 24:
    hours -= 24
if minutes // 10 == 0 and minutes > 0 :
    minutes = "0" + str(minutes)
if seconds // 10 == 0 and seconds > 0 :
    seconds = "0" + str(seconds)
print(f"{hours}:{int(minutes):02d}:{int(seconds):02d}")