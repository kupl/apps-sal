from math import log

def next_day_of_week(current_day, available_week_days):
    code = bin(available_week_days)[2:].rjust(7, "0")[::-1]
    for i in range(current_day, 7):
        if code[i] == "1":
            return i + 1
    for i in range(current_day):
        if code[i] == "1":
            return i + 1

