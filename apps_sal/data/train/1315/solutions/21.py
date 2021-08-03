# cook your dish here
n = int(input())
l = []
for i in range(n):
    x = list(map(int, input().split()))
    x.sort(reverse=True)
    l.append(x)
s = 0
for i in range(n):
    c = 0
    for j in range(n):
        if(l[i] == l[j]):
            c += 1
    if(c == 1):
        s += 1
print(s)
