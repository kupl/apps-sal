def get_average(marks):
    total_marks = 0
    for i in marks:
        total_marks += i
    average = total_marks / len(marks)
    return int(average)

