# 555A
# θ(n) time
# O(n) space

__author__ = 'artyom'


# SOLUTION

def main():
    n, k = read(3)
    c = 0
    l = 1
    for _ in range(k):
        a = read(3)
        if a[1] == 1:
            j = 1
            while j < a[0] and a[j + 1] - a[j] == 1:
                j += 1
                l += 1
            c += a[0] - j
        else:
            c += a[0] - 1
    return c + n - l


# HELPERS

def read(mode=1, size=None):
    # 0: String
    # 1: Integer
    # 2: List of strings
    # 3: List of integers
    # 4: Matrix of integers
    if mode == 0:
        return input().strip()
    if mode == 1:
        return int(input().strip())
    if mode == 2:
        return input().strip().split()
    if mode == 3:
        return list(map(int, input().strip().split()))
    a = []
    for _ in range(size):
        a.append(read(3))
    return a


def write(s="\n"):
    if s is None:
        s = ''
    if isinstance(s, tuple) or isinstance(s, list):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end="\n")


write(main())
