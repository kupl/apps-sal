# cook your dish here
t = int(input())
while t != 0:
    n = int(input())
    a = list(map(int, input().split()))[:n]
    happy = False
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] != a[j]:
                k, r = a[i], a[j]
                if a[k - 1] == a[r - 1]:
                    happy = True
                    break
    if happy == True:
        print('Truly Happy')
    else:
        print('Poor Chef')
    t -= 1
