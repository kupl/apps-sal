import sys

input = sys.stdin.readline
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())


def main():
    h, w = MI()
    s = [[c == "
    t = [[-1] * (w - 1) for _ in range(h - 1)]
    for i in range(h - 1):
        si = s[i]
        si1 = s[i + 1]
        t[i] = [1 - (sum(si[j:j + 2]) + sum(si1[j:j + 2])) % 2 for j in range(w - 1)]
    ti = t[0]
    for i in range(1, h - 1):
        ti1 = ti
        ti = t[i]
        for j in range(w - 1):
            if ti[j]:
                ti[j] = ti1[j] + 1
    ans = 0
    for i in range(h - 1):
        jtol = [0] * (w - 1)
        jtor = [0] * (w - 1)
        ti = t[i]
        stack = [[-1, 0]]
        for j in range(w - 1):
            tij = ti[j]
            while stack[-1][0] >= tij:
                stack.pop()
            jtol[j] = stack[-1][1]
            stack.append([tij, j + 1])

        stack = [[-1, w - 1]]
        for j in range(w - 2, -1, -1):
            tij = ti[j]
            while stack[-1][0] >= tij:
                stack.pop()
            jtor[j] = stack[-1][1]
            stack.append([tij, j])

        for j in range(w - 1):
            tmp = (jtor[j] - jtol[j] + 1) * (ti[j] + 1)
            if tmp > ans:
                ans = tmp
    print(max(ans, h, w))


main()
