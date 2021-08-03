def istriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a + b < c) or (a + c < b) or (b + c < a):
        return False
    else:
        return True


def valid(a, b, n):
    if a[0] != 0 or b[-1] != 0 or a[-1] != b[0]:
        return False
    for i in range(1, n - 1):
        if not istriangle(a[-1], a[i], b[i]):
            return False
    return True


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if valid(a, b, n):
        print('Yes')
    else:
        print('No')
