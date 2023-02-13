"""Create a random password generator using loops"""

student_heights = [180, 124, 165, 173, 189, 169, 146]
max_number = 0

for i in student_heights:
    if i > max_number:
        max_number = i
print(f"The highest score in the class is: {max_number}")