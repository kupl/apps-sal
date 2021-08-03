t = int(input())
a = "abcdefghijklmnopqrstuvwxyz"
for i in range(t):
    c = 0
    p = input().split()
    s = input()

    for j in range(len(a)):
        if(a[j] not in s):
            c = c + int(p[j])
    print(c)
