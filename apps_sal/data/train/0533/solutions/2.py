# cook your dish here
for t in range(int(input())):
    k, n = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    lst = []
    for i in range(n):
        if a[i] == k:
            lst.append(i)
    if len(lst) > 0:
        print(max(lst) - min(lst))
    else:
        print(0)
