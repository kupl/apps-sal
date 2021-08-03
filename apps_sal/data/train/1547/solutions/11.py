vacc = 0
day = 0
d1, v1, d2, v2, p = list(map(int, input().split()))
for i in range(1, 1000):
    if i >= d1:
        vacc = vacc + v1
    if i >= d2:
        vacc = vacc + v2
    day = day + 1
    if vacc >= p:
        break
print(day)
