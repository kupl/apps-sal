def super_size(n):
    a = []
    for i in range(len(str(n))):
        a.append(n%10)
        n //= 10
    a = list(reversed(sorted(a)))
    num = 0
    for i in a:
        num = num * 10 + i
    return num
