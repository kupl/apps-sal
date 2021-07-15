def get_average(marks):
    #raise NotImplementedError("TODO: get_average")
    average = 0
    for a in marks:
        average += a
    return int(average/len(marks))
