# Write a program to control entrance to a club.
# Only people who are 18 or older are allowed to enter the club.
# Your program takes the age of the person who tries to enter,
# and outputs "Allowed" if they are allowed to enter the club,
# and "Sorry" if they are younger than the allowed age.

age = int(input())
if age > 17:
    print("Allowed")
elif age < 18:
    print("Sorry")
# else:
#     print("Just wanted to add else for retention's sake")
