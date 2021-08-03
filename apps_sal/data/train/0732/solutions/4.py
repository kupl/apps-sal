# cook your dish here
def walk(n, m, o):
    a = 0
    b = 0
    tot = 0
    for i in range(n):
        if((m[i] == o[i]) and (a == b)):
            tot += m[i]
        a += m[i]
        b += o[i]
    return tot


t = int(input())
for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    o = list(map(int, input().split()))
    print(walk(n, m, o))
