"""
    Author      : Arif Ahmad
    Date        : 
    Algo        : 
    Difficulty  : 
"""
from sys import stdin, stdout, setrecursionlimit
import threading


def main():
    m = int(stdin.readline().strip())
    a = [int(_) for _ in stdin.readline().strip().split()]
    b = [int(_) for _ in stdin.readline().strip().split()]

    c = []
    for i, v in enumerate(b):
        c.append((v, i))

    a = sorted(a, reverse=True)
    c = sorted(c)

    ans = [0 for i in range(m)]
    j = 0
    for v, i in c:
        ans[i] = a[j]
        j += 1

    stdout.write(' '.join(str(_) for _ in ans))


def __starting_point():
    setrecursionlimit(10**6)
    threading.stack_size(134217728)
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
