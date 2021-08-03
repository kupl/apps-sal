def get_average(marks):
    sum = 0
    for i in marks:
        sum = sum + i

    average = sum / len(marks)
    return int(average)

    raise NotImplementedError("didn't work for" + marks)


print((get_average([2, 2, 2, 2])))
print((get_average([1, 5, 87, 45, 8, 8])))
