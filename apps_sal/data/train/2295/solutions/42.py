N = int(input())
ans = 0
a_chance = 0
a_remain = []
b_remain = []
for i in range(N):
    (a, b) = map(int, input().split())
    if b >= a:
        ans += b
        a_chance += b - a
    else:
        a_remain.append(a)
        b_remain.append(b)
if a_chance == 0:
    print(0)
else:
    print(ans + sum(b_remain) - min(b_remain))
