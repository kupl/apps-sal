def add(*args):
    sum = 0
    for idx, num in enumerate(args):
        sum += (num / (idx + 1.0))
    return round(sum)
    # your code here
