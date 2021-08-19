def avg(seq):
    sum = 0
    count = 0
    for i in seq:
        sum += i
        count += 1
    return sum / count if count != 0 else 0


def sum_average(arr):
    return __import__('math').floor(sum((avg(i) for i in arr)))
