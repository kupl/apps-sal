S, T = input(), input()
q = int(input())

ls, lt = len(S), len(T)
acs, act = [0] * (ls + 1), [0] * (lt + 1)

for i in range(1, ls + 1):
    acs[i] = acs[i - 1] + (S[i - 1] == "A")
for i in range(1, lt + 1):
    act[i] = act[i - 1] + (T[i - 1] == "A")

for _ in range(q):
    a, b, c, d = list(map(int, input().split()))
    sa = acs[b] - acs[a - 1]
    sb = b - a + 1 - sa
    ta = act[d] - act[c - 1]
    tb = d - c + 1 - ta
    print(("YES" if (2 * sa + sb) % 3 == (2 * ta + tb) % 3 else "NO"))
