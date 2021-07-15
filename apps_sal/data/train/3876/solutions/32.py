def find(n):
    # up to, including n
    # range(n +1)
    # iterate over number
    # if divisible by 3 or 5
    # add to total
    total = 0
    for num in range(n+1):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total
