n = int(input())
r = input()
r1 = input()
ans1 = 0
ans0 = 0
c1 = 0
c0 = 0
for i in range(n):
    if (r1[i] == "0"):
        if (r[i] == "0"):
            c0 = c0 + 1
        else:
            c1 = c1 + 1
    else:
        if (r[i] == "0"):
            ans0 = ans0 + 1
        else:
            ans1 = ans1 + 1
fans = c0 * ans1 + c1 * ans0 + (c0 * c1)
print(fans)
