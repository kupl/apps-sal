def get_average(marks):
    a = len(marks)
    b = 0
    for i in range(0, len(marks)):
        b = b + marks[i]
    average = int(b / a)
    return average
#    raise NotImplementedError("TODO: get_average")
