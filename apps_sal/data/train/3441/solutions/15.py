def get_average(marks):
    sum = 0
    for x in marks:
        sum = sum + x
    num = len(marks)
    ans = sum / num
    return int(ans)
