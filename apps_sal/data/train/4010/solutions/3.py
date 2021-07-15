from itertools import combinations
def counting_triangles(V):
    count = 0
    for i in combinations(V,3):
        i = sorted(i)
        if i[0]+i[1] > i[2]:
            count += 1
    return count
