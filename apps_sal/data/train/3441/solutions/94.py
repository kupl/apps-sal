def get_average(marks):
    answer = 0
    for grades in marks:
        answer += grades
    return answer // len(marks)
