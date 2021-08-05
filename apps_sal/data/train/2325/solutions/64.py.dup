s = input()
t = input()
cs = [0]
for i in s:
    if i == "A":
        cs.append((cs[-1] + 1) % 3)
    else:
        cs.append((cs[-1] + 2) % 3)
ct = [0]
for i in t:
    if i == "A":
        ct.append((ct[-1] + 1) % 3)
    else:
        ct.append((ct[-1] + 2) % 3)

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    if (cs[b] - cs[a - 1]) % 3 == (ct[d] - ct[c - 1]) % 3:
        print("YES")
    else:
        print("NO")
