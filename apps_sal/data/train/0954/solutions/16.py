# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = [x for x in range(1, n + 1)]
    su = [n]
    summ = 0
    for i in range(len(s) - 1):
        su.append(s[i])
        su.append(s[i])
    for x in range(len(su)):
        summ += su[x] ** 3
    print(summ)
