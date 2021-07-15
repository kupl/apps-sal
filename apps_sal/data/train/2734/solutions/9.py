def peaceful_yard(yard, min_distance):
    from scipy.spatial.distance import euclidean

    cat_positions = [(i, j) for i in range(len(yard)) 
                     for j in range(len(yard[i])) if yard[i][j] in "LMR"]

    from itertools import combinations
    return all(euclidean(cat1, cat2) >= min_distance 
               for cat1, cat2 in combinations(cat_positions, 2))

