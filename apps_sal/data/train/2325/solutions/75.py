s = input().strip()
t = input().strip()
SX = [0]
for c in s:
    if c == "A":
        SX.append(SX[-1] + 1)
    else:
        SX.append(SX[-1])
TX = [0]
for c in t:
    if c == "A":
        TX.append(TX[-1] + 1)
    else:
        TX.append(TX[-1])

Q, = list(map(int, input().split()))
for _ in range(Q):
    a, b, c, d = list(map(int, input().split()))
    sa = SX[b] - SX[a - 1]
    sb = b - a + 1 - sa
    ta = TX[d] - TX[c - 1]
    tb = d - c + 1 - ta
#    print(sa, sb, ta, tb)
    if (sa - sb) % 3 == (ta - tb) % 3:
        print("YES")
    else:
        print("NO")
