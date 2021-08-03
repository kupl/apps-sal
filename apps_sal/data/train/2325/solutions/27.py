S = input()
T = input()
q = int(input())

S_rel_idx = [0]
T_rel_idx = [0]

for s in S:
    if s == "A":
        S_rel_idx.append((S_rel_idx[-1] + 1) % 3)
    else:
        S_rel_idx.append((S_rel_idx[-1] - 1) % 3)

for t in T:
    if t == "A":
        T_rel_idx.append((T_rel_idx[-1] + 1) % 3)
    else:
        T_rel_idx.append((T_rel_idx[-1] - 1) % 3)
# print(S_rel_idx)
# print(T_rel_idx)
for _ in range(q):
    a, b, c, d = list(map(int, input().split()))

    if (S_rel_idx[b] - S_rel_idx[a - 1]) % 3 == (T_rel_idx[d] - T_rel_idx[c - 1]) % 3:
        print("YES")
    else:
        print("NO")
