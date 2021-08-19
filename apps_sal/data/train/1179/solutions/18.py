import math
t = int(input())
for test in range(t):
    n = int(input())
    sum_array = n * (n + 1) // 2
    if sum_array % 2 != 0:
        print(0)
        continue
    ideal_sum = sum_array // 2
    partition_sum = 0
    partition_ind = 0
    n_swap = 0
    for i in range(1, n + 1):
        if i + partition_sum > ideal_sum:
            partition_ind = i - 1
            break
        else:
            partition_sum += i
    n_swap = n - partition_ind
    f = math.factorial
    if partition_sum == ideal_sum:
        if partition_ind >= 2:
            n_swap += f(partition_ind) // 2 // f(partition_ind - 2)
        if n - partition_ind >= 2:
            n_swap += f(n - partition_ind) // 2 // f(n - partition_ind - 2)
    print(n_swap)
