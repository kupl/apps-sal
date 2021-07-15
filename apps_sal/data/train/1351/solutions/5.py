# cook your dish here
n = input()
for i in range(int(n)):
    k = int(input())
    l = list(map(int,input().split()))
    f = []
    for i in range(k):
        if i in l:
            f.append(i)
        else:
            f.append(0)
    print(*f)

