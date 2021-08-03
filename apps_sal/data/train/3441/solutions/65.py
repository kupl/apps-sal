def get_average(marks):

    sum = 0
    mylen = len(marks)
    for x in marks:
        sum = sum + x

    avg = sum / mylen
    return int(avg)
