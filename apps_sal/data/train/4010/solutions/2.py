import itertools


def counting_triangles(V):
    count = 0
    for x in itertools.combinations(V, 3):
        if(sum([x[0] + x[1] > x[2], x[0] + x[2] > x[1], x[1] + x[2] > x[0], abs(x[0] - x[1]) < x[2], abs(x[0] - x[2]) < x[1], abs(x[1] - x[2]) < x[0]]) == 6):
            count += 1
    return count
