n, m, k = input().split(" ")
l = []
c1 = 0
while(int(n) > 0):
    s = 0
    l = input().split(" ")
    for i in range(0, int(k)):
        s = s + int(l[i])
    if(s >= int(m) and int(l[-1]) <= 10):
        c1 = c1 + 1
    n = int(n) - 1
print(c1)
