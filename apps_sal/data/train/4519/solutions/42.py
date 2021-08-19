def max_number(n):
    arr = list(str(n))
    result = []
    for i in arr:
        result.append(i)
    num = sorted(result)
    num.reverse()
    out = ''.join(num)
    return int(out)
