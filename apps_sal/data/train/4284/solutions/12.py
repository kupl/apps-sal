def array_leaders(numbers):
    sum = 0
    (i, l) = (1, len(numbers))
    leaders = []
    while i <= l:
        if numbers[-i] > sum:
            leaders = [numbers[-i]] + leaders
        sum += numbers[-i]
        i += 1
    return leaders
