def blocks_to_collect(level):
    (order, output, count) = (['gold', 'diamond', 'emerald', 'iron'], {'total': 0, 'gold': 0, 'diamond': 0, 'emerald': 0, 'iron': 0}, 3)
    for loop in range(level):
        square = count * count
        output['total'] += square
        output[order[loop % 4]] += square
        count += 2
    return output
