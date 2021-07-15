res, a = [], []
 
 
def rot(i: int) -> None:
    nonlocal res, a
    res.append(i + 1)
    a[i], a[i+1], a[i+2] = a[i+2], a[i], a[i+1]
    #print(f'Rotation on {i}: {a}')
 
 
def solve():
    nonlocal res, a
    res.clear()
    input()
    a = [int(i) for i in input().split()]
    s = sorted(a)
    for i in range(len(a) - 2):
        if a[i] == s[i]:
            continue
        j = a.index(s[i], i, len(a))
        while j != i:
            if j - i >= 2:
                j -= 2
                rot(j)
            else:
                rot(i)
                j += 1
    if any(a[i] > a[i + 1] for i in range(len(a) - 1)):
 
        for i in range(len(a) - 3, -1, -1):
            while a[i + 2] < a[i] or a[i + 2] < a[i + 1]:
                rot(i)
 
        if all(a[i] != a[i + 1] for i in range(len(a) - 2)):
            print(-1)
            return
 
    print(len(res))
    print(' '.join(str(i) for i in res))
 
 
t = int(input())
while t > 0:
    t -= 1
    solve()
