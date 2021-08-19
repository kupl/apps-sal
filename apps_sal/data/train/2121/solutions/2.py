# Тупо скопировал решение, ибо никак не пойму поверить в решение за менее чем 1 #секунду(((

from sys import stdin


def run(n, s):
    m = 0
    small = n // 2
    for big in range(n - 1, (n + 1) // 2 - 1, -1):
        while small >= 0 and s[small] > s[big] / 2:
            small -= 1
        if small == -1:
            break
        small -= 1
        m += 1
    print(n - m)


n = int(input())
s = sorted([int(x) for x in stdin.read().strip().split('\n')])
run(n, s)
