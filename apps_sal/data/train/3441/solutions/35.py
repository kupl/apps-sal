def get_average(marks):
    import math
    n = 0
    for i in marks:
        n += i
    result = n / len(marks)
    result = math.floor(result)
    return result
