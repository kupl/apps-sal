# cook your dish here
t = int(input())

for i in range(t):

    n, k = map(int, input().split())

    x = list(map(int, input().split()))
    c = 0
    for j in x:
        j += k
        if j % 7 == 0:
            c += 1
    print(c)
