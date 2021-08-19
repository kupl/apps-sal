def get_average(marks):
    total = 0
    for i in marks:
        total = total + i
    avg = total // len(marks)
    return avg

# alternatively
# from statistics import mean as m
# from math import floor as f

# def get_average(marks):
#     avg = m(marks)
#     return f(avg)
