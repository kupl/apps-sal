# write your code in next line.
a = int(input())
while(a):
    b = int(input())
    c = str(input()).split()
    d = str(input())
    l = 0
    m = 0
    x = 0
    while(b):
        l = c[b - 1].count(d)
        if l >= x:
            x = l
            m = c[b - 1]
        b -= 1
    a -= 1
    print(m)
