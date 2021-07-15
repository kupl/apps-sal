def max_tri_sum(numbers):
    maximums = []
    while len(maximums) < 3:
        if max(numbers) not in maximums:
            maximums.append(max(numbers))
        else:
            numbers.remove(max(numbers))
    return sum(maximums)
