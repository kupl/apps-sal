students = []
for i in range(int(input())):
  students.append([i, sum(map(int, input().split()))])

students.sort(key=lambda x:(-x[1], x[0]))
for i, student in enumerate(students):
  if student[0] == 0:
    print(i+1)
    break


