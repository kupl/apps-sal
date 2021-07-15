s = '0'
s += input()


def isPara(string, l, r):
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def solve():
    N = len(s)-1
    if s[N] == '1' or s[1] == '0':
        print((-1))
        return
    if isPara(s, 1, N-1) == False:
        print((-1))
        return
    root = 1
    for i in range(2, N+1):
        print((str(root) + ' ' + str(i)))
        if s[i-1] == '1':
            root = i


solve()

