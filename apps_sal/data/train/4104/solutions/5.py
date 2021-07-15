def max_tri_sum(numbers):
    sorted_n = sorted(numbers, reverse=True)
    triplet = [sorted_n[0]]
    count = 1
    for n in sorted_n[1:]:
        if count == 3: break
        if n not in triplet:
            triplet = triplet + [n]
            count += 1
    return sum(triplet)
