def digitize(n):
    ls = []
    for i in range(len(str(n))):
        ls.append(n % 10)
        n //= 10
    return ls
