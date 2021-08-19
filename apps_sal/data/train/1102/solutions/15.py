d = {1: 1, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 4, 8: 3, 9: 4, 0: 1}
n = int(input())
for i in range(n):
    p = int(input())
    sum = 1
    if p < 9:
        print(d[p])
    else:
        r = str(p)
        for j in range(len(r)):
            sum = sum * d[int(r[j])]
        print(sum % 1000000007)
