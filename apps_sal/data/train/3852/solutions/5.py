def ips_between(start, end):
    difference = [int(b) - int(a) for (a, b) in zip(start.split('.'), end.split('.'))]
    sum = 0
    for d in difference:
        sum *= 256
        sum += d
    return sum
