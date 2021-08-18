def meters(x):
    arr = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    count = 0
    while x >= 1000:
        x /= 1000.00
        count += 1
    if int(x) == x:
        x = int(x)
    return str(x) + arr[count] + 'm'
