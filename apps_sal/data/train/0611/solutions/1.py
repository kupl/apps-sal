# cook your dish here

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] - 1 not in d:
            d[a[i] - 1] = [i]
        else:
            d[a[i] - 1].append(i)
    ans = False
    d1 = {}
    for i in range(len(a)):
        d1[i] = a[i]
    for i in d:
        if ans == True:
            break
        for j in d:
            if i != j:
                if d1[i] == d1[j] and i != j:
                    ans = True
                    break
    if ans == True:
        print('Truly Happy')
    else:
        print('Poor Chef')
