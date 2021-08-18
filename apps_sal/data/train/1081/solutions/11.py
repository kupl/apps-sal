from sys import stdin
def input(): return stdin.readline().rstrip("\r\n")


def inp(): return list(map(int, stdin.readline().rstrip("\r\n").split()))


tc = 1
tc, = inp()
for _ in range(tc):
    s = str(input())
    d = [98, 57, 31, 45, 46]
    a = [ord(i) - ord('A') for i in s]
    d = [(a[i] + d[i]) % 26 for i in range(len(s))]
    ans = [chr(i + ord('A')) for i in d]
    print(''.join(ans))
