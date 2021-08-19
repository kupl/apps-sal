def artificial_rain(garden):
    with_left_wall_at = 0
    best_coverage = coverage = 1
    for i in range(1, len(garden)):
        height = garden[i]
        left_neighbor_height = garden[i - 1]
        if left_neighbor_height > height:
            with_left_wall_at = i
        elif left_neighbor_height < height:
            if coverage > best_coverage:
                best_coverage = coverage
            coverage = i - with_left_wall_at
        coverage += 1
    if coverage > best_coverage:
        best_coverage = coverage
    return best_coverage
