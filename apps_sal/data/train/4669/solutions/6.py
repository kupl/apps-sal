def beggars(values, n):
    # your code here
    if n == 0:
        return []
    newe = list(0 for i in range(n))
    count = 0
    for i in values:
        newe[(count % n)] += i
        count += 1
    return newe
