from itertools import product


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def cluster(points, n):
    lista = [[en] for en in points]
    while len(lista) > n:
        (min_pair, min_dist) = ((0, 0), float('inf'))
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                dist = 0
                pairs = list(product(lista[i], lista[j]))
                for pair in pairs:
                    dist += distance(pair[0], pair[1])
                dist /= len(pairs)
                if dist < min_dist:
                    min_dist = dist
                    min_pair = (i, j)
        lista[min_pair[0]].extend(lista[min_pair[1]])
        del lista[min_pair[1]]
    lista = [sorted(en) for en in lista]
    return sorted(lista, key=lambda x: x[0])
