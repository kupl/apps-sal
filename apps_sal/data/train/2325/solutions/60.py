S = input()
T = input()
rui_s = [0]
rui_t = [0]
for s in S:
    if s == "A":
        rui_s.append((rui_s[-1] + 1) % 3)
    else:
        rui_s.append((rui_s[-1] + 2) % 3)
for t in T:
    if t == "A":
        rui_t.append((rui_t[-1] + 1) % 3)
    else:
        rui_t.append((rui_t[-1] + 2) % 3)
        
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if (rui_s[b] - rui_s[a - 1]) % 3 == (rui_t[d] - rui_t[c - 1]) % 3:
        print("YES")
    else:
        print("NO")
