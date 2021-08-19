t = int(input())
while t:
    par = [int(i) for i in input().split(' ')]
    (a, d, l, r) = (par[0], par[1], par[2], par[3])
    elem_array = []
    cycle_sum = 0
    for i in range(0, 9):
        elem_array.append(1 + (a + i * d - 1) % 9)
        cycle_sum = cycle_sum + elem_array[i]
    ans = 0
    if r - l > 8:
        total_cycle = (r - l + 1) / 9
        ans = ans + cycle_sum * total_cycle
        l = l + total_cycle * 9
        while l <= r:
            ans = ans + elem_array[(l - 1) % 9]
            l = l + 1
    elif r - l == 8:
        ans = cycle_sum
    else:
        while l <= r:
            ans = ans + elem_array[(l - 1) % 9]
            l = l + 1
    print(ans)
    t -= 1
