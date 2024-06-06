""" 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
"""

student_pet_count = [0, 1, 2, 3, 1, 2, 1, 2, 1, 2, 2, 2]

NUM_OF_STUDENTS = len(student_pet_count)
print(NUM_OF_STUDENTS)

# avg = sum / total

ITEM_THREE_FROM_BACK = student_pet_count[-3]
# print(ITEM_THREE_FROM_BACK)

SUM = 0

for INDIVIDUAL_PET_COUNT in student_pet_count:
  SUM = SUM + INDIVIDUAL_PET_COUNT
print(SUM)

AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)