n = int(input())
a, ar, b, br = 0, 0, 0, 0
for i in range(n):
    x = list(map(int, input().split()))
    if(x[0] == 1):
        a += 10
        ar += x[1]
    else:
        b += 10
        br += x[1]
print('DLEIAVDE'[ar >= a // 2::2])
print('DLEIAVDE'[br >= b // 2::2])
