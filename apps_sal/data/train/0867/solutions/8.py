# cook your dish here
a = int(input())
for i in range(a):
    l = list(map(int, input().split()))
    k = l[0]
    l.remove(l[0])
    b = 0
    for i in range(len(l) - 1):
        c = l[i]
        if(c <= k):
            b += 1
        c = c + l[i + 1]
    print(b)
