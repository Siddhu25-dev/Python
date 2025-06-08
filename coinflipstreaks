print("Name: Siddharth A Gurav")
print("USN: 1AY24AI107")
print("Section: O")
import random
flips = int(input("Enter the number of coin flips: "))
results = []
streak = 0
max_streak = 0
for _ in range(flips):
    flip = random.choice(['H', 'T'])
    results.append(flip)
    if len(results) > 1 and results[-1] == results[-2]:
        streak += 1
    else:
        streak = 1
    if streak > max_streak:
        max_streak = streak
print("Results:", results)
print("Longest streak:", max_streak)
