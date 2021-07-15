def blocks_to_collect(level):
    seq = ['gold', 'diamond', 'emerald', 'iron']
    result = {
        "total": 0, 
        "gold": 0, 
        "diamond": 0, 
        "emerald": 0, 
        "iron": 0
    }
    for i in range(1, level + 1):
        n = (i * 2 + 1) ** 2
        result['total'] += n
        result[seq[(i - 1) % len(seq)]] += n
    return result
