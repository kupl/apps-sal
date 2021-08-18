t_cases = int(input())
for i in range(t_cases):
    n_cars = int(input())
    max_speeds = list(map(int, input().split()))
    res = 0
    for j in range(n_cars - 1):
        if max_speeds[j + 1] > max_speeds[j]:
            max_speeds[j + 1] = max_speeds[j]
            res += 1
    print(n_cars - res)
