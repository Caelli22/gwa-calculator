grades = []
unit = []
total_grades = 0.0
total_units = 0.0
grade_times_unit = []
total_grade_times_unit = 0.0

sub = input("Enter how many Subjects: ")

for i in range(int(sub)):
    sub_grade = input(f"Enter grade in subject {i}: ")
    sub_unit = input(f"Enter unit in subject {i}: ")
    grades.append(float(sub_grade))
    unit.append(float(sub_unit))
    grade_x_unit = float(sub_grade) * float(sub_unit)
    grade_times_unit.append(float(grade_x_unit))

for i in range(int(sub)):
    total_grades = total_grades + grades[i]
    total_units = total_units + unit[i]
    total_grade_times_unit = total_grade_times_unit + grade_times_unit[i]

gwa = total_grade_times_unit / total_units
print()
print(f"Your GWA is {gwa}")