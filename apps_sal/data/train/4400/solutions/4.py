def minimum_steps(numbers, value):
    sorted_n = sorted(numbers)
    (n, sum) = (0, sorted_n[0])
    for i in sorted_n[1:]:
        if sum >= value:
            break
        sum += i
        n += 1
    return n
