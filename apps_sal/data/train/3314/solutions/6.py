def solve(a, b):
    b1 = b
    answer = True
    i = 2
    primfac = []
    while i * i <= b:
        while b1 % i == 0:
            primfac.append(i)
            b1 = b1 // i
        i = i + 1
    if b1 > 1:
        primfac.append(b1)
    for i in range(0, len(primfac)):
        if a % primfac[i] != 0:
            answer = False
    return answer
