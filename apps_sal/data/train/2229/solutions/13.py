a = input()
b = input()
c = [i - 1 for i in list(map(int, input().split()))]
l = 0
r = len(a)
while r - l > 1:
    m = l + (r - l) // 2
    t = list(a)
    j = 0
    for i in range(m):
        t[c[i]] = ''
    for i in range(len(a)):
        if t[i] == b[j]:
            j += 1
            if j == len(b):
                l = m
                break
    if j != len(b):
        r = m
print(l)


# Made By Mostafa_Khaled
