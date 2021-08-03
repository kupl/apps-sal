def consecutive_sum(num):
    sol = 1
    nums = 1
    i = 2
    while num > nums:
        if (num - nums) % i == 0:
            sol += 1
        nums += i
        i += 1

    return sol
