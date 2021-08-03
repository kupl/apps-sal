# cook your dish here
n = int(input())
i = 0
s1 = 0
s2 = 0
m = 0
w = 0
while i < n:
    a, b = input().split()
    a = int(a)
    b = int(b)
    s1 += a
    s2 += b
    if s1 > s2:
        l = s1 - s2
        if l > m:
            m = l
            w = 1
    else:
        l = s2 - s1
        if l > m:
            m = l
            w = 2
    i += 1
print(w, m)
