__author__ = 'artyom'


def main():
    (n, k) = read(3)
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


def read(mode=1, size=None):
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


def write(s='\n'):
    if s is None:
        s = ''
    if isinstance(s, tuple) or isinstance(s, list):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end='\n')


write(main())
