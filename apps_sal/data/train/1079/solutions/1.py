t = int(input())
for i in range(t):
    v = input()
    l = len(v)
    d = "4"
    c = 0
    for i in range(l):
        if(v[i] == d):
            c += 1
    print(c)
