t = int(input())
for i in range(t):
    (candies, student) = map(int, input().split())
    if student == 0:
        print(0, candies)
    else:
        each_student = candies // student
        teachers = candies % student
        print(each_student, teachers)
