t = eval(input())
for qq in range(t):
    n, m, z, l, r, b = list(map(int, input().split()))
    seat_max = n * m
    seat_used = l + r + z
    armrest_max = n * (m + 1)
    armrest_used = l + r
    if (seat_used >= seat_max):
        print(seat_max)
    else:
        armrest_used_by_b = (armrest_max - armrest_used) / 2
        seat_used_by_b = min(armrest_used_by_b, b, ((m + 1) / 2) * n)
        seat_used += seat_used_by_b
        print(min(seat_used, seat_max))
