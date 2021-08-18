from collections import deque


def cxx2(x):
    if(x <= 1):
        return 0
    elif(x == 2):
        return 1
    else:
        sans = 1
        for i in range(x - 1, x + 1):
            sans *= i
        sans //= 2
        return sans


def cxx3(x):
    if(x <= 2):
        return 0
    elif(x == 3):
        return 1
    else:
        sans2 = 1
        for i in range(x - 2, x + 1):
            sans2 *= i
        sans2 //= 6
        return sans2


'''for i in range(10):
    print(cxx2(i))'''
inp = input().split()
n = int(inp[0])
d = int(inp[1])
inp = input().split()
a = deque()
ans = 0
for i in range(n):
    a.append(int(inp[i]))
    if(len(a) != 0):
        while(a[-1] - a[0] > d):
            a.popleft()
            ans += cxx2(len(a) - 1)
while(len(a) != 0):
    a.popleft()
    ans += cxx2(len(a))
print(ans)
