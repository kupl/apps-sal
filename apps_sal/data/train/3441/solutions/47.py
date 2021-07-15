
def get_average(marks):
    avg = 0
    for elem in marks:
        avg += elem
    avg = avg / len(marks)
    
    return int(avg)

