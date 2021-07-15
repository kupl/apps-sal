def get_average(marks):
    total = 0 
    for x in marks:
        total += x 
    return round(int(total / len(marks)))
