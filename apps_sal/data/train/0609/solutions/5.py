# cook your dish here
t = int(input())
# print(t)
for _ in range(t):
    # print(t)
    p = list(map(int, input().split()))
    n = p[0]
    k = p[1]
    l = list(map(int, input().split()))
    # print(l)
    s = 0
    f = 1
    for i in range(0, n):
        s += l[i]
        if(s < k):
            print(i + 1)
            f = 0
            break
        s = s - k

    if(f):
        print(sum(l) // k + 1)
