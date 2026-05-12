# Day 2 - If Else and Input
# Author: Mohammad Musab

print("=== Day 2: Decision Making ===")

# 1. Equality check with if-else
number_of_followers = 100
if number_of_followers == 100:
    print("You are famous!")
else:
    print("You're not famous yet")

# 2. Greater than check
number_of_comments = 150
if number_of_comments > 100:
    print("You are going viral")
else:
    print("Keep posting")

# 3. Taking number input from user
print("Enter your age:")
age = int(input())
print("Next year your age will be:")
print(age + 1)

# 4. Grade system with elif
print("Enter your marks:")
marks = int(input())

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: Fail. Try again")

print("=== Day 2 Complete ===")
print("Logic Building: Unlocked")
print("Google CEO Level: 2 Clear")
