
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


T = int(input())
while T:
    a, b, N = map(int, input().split())
    c = set()
    ls = []
    for i in range(1, N + 1):
        for j in range(1, i):
            k = gcd(i, j)
            if(j / i not in c):
                c.add(j / i)
                ls.append([j / i, j // k, i // k])
    ls.sort()
    for i in range(len(ls)):
        if(ls[i][1] == a and ls[i][2] == b):
            break
    print(ls[i - 1][1], ls[i - 1][2])
    T -= 1
