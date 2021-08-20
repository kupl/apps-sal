def main():
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    d = dict()
    d1 = {}
    for i in s:
        d[i] = [l.index(i), False]
        d1[i] = 1
    for i in range(n):
        if d[l[i]][1] == False:
            d[l[i]][1] = True
            continue
        elif d[l[i]][0] + 1 != i:
            d1[l[i]] += 1
            d[l[i]][0] = i
    maxi = 0
    for i in d1.values():
        if i > maxi:
            maxi = i
    for i in sorted(d1):
        if d1[i] == maxi:
            print(i)
            break


for _ in range(int(input())):
    main()
