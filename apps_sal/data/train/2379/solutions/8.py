mod = 10 ** 9 + 7


def solve():
    n = int(input())
    s = input()
    s0 = []
    s1 = []
    vec = []
    sm = 0
    for i in range(n):
        if s[i] == '1':
            if len(s0) < 1:
                sm += 1
                s1.append(sm)
                vec.append(sm)
            else:
                vec.append(s0[len(s0) - 1])
                s1.append(s0[len(s0) - 1])
                s0.pop()
        elif len(s1) < 1:
            sm += 1
            s0.append(sm)
            vec.append(sm)
        else:
            vec.append(s1[len(s1) - 1])
            s0.append(s1[len(s1) - 1])
            s1.pop()
    print(sm)
    print(*vec, sep=' ')


t = 1
t = int(input())
for _ in range(t):
    solve()
