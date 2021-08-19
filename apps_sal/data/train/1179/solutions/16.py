# cook your dish here
import math
t = int(input())
for test in range(t):
    n = int(input())
    # If total sum is not even, then we cant divide array in 2 equal sum arrays
    sum_array = (n * (n + 1)) // 2
    if sum_array % 2 != 0:
        print(0)
        continue
    # 1 2 3 4 5 6 7 8 --  9 10 11 12  ---> divide closest to ideal sum

    n_swap = 0
    d = 1 + 4 * sum_array
    partition_ind = (math.sqrt(d) - 1) / 2
    n_swap = n - math.floor(partition_ind)
    f = math.factorial
    if partition_ind.is_integer():
        partition_ind = int(partition_ind)
        if partition_ind >= 2:
            n_swap += (f(partition_ind) // 2 // f(partition_ind - 2))
        if n - partition_ind >= 2:
            n_swap += (f(n - partition_ind) // 2 // f(n - partition_ind - 2))

    print(n_swap)
