n = int(input())
for i in range(n):
    m = int(input())
    l = list(map(int, str(m)))
    sum = 0
    for j in range(len(l)):
        sum = sum + pow(l[j], len(l))
    if sum == m:
        print('FEELS GOOD')
    else:
        print('FEELS BAD')
