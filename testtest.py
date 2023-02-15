from statistics import mean

points = []
grades = "FFFFFCCBAAA"
input("Enter student name: ")
points.append(int(input("Enter math point (100): ")))
points.append(int(input("Enter physics point (100): ")))
points.append(int(input("Enter programming point (100): ")))
meanPoint = mean(points)
print(f"Your average point is {meanPoint}")
print(f"Your grade is {grades[int(meanPoint/10)]}")