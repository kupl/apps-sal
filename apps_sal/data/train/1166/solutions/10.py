# cook your dish here
n = int(input())
s1 = input().split(' ')
l = []
for _ in s1:
    l.append(int(_))
i = 0
sub = []
while(i < n):
    s = i
    f = i + 1
    while(f <= n):
        l1 = l[s:f]
        sub.append(l1)
        f += 1
    i += 1

q = int(input())
k = 0
while(k < q):
    c = 0
    q1 = int(input())
    for e in sub:
        if(min(e) == q1):
            c += 1
    print(c)
    k += 1
