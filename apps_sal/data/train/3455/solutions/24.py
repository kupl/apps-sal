def disarium_number(n):
    x = [int(x)for x in str(n)]
    s = 0
    for i in range(len(str(n))):
        s = s + x[i]**(i + 1)
    return 'Disarium !!'if s == n else 'Not !!'
