from statistics import mean
from itertools import product
from math import sqrt, inf


def distance_between_points(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def distance_between_clusters(cluster1, cluster2):
    return mean(
        distance_between_points(point1, point2) for (point1, point2) in product(cluster1, cluster2)
    )


def merge_clusters(cluster1, cluster2):
    return sorted([*cluster1, *cluster2])


def identificator(cluster):
    return (cluster[0], len(cluster))


def update_distances(clusters, distances):
    for cluster1 in clusters:
        for cluster2 in clusters:
            id1 = identificator(cluster1)
            id2 = identificator(cluster2)
            if id1 != id2 and distances.get((id1, id2)) is None:
                distance = distance_between_clusters(cluster1, cluster2)
                distances[(id1, id2)] = distance
                distances[(id2, id1)] = distance


def clear_unactual_distances(distances, cluster1, cluster2):
    old_ids = [identificator(cluster1), identificator(cluster2)]
    new_distances = {k: v for k, v in list(distances.items()) if k[0] not in old_ids and k[1] not in old_ids}
    return new_distances
                

def pop_minimal_distance_pair(clusters, distances):
    minimal_ids = None
    minimal_distance = 10_000_000
    for ids_pair, distance in list(distances.items()):
        if distance < minimal_distance:
            minimal_distance = distance
            minimal_ids = ids_pair
    cluster1 = next(cluster for cluster in clusters if identificator(cluster) == minimal_ids[0])
    cluster2 = next(cluster for cluster in clusters if identificator(cluster) == minimal_ids[1])
    clusters.remove(cluster1)
    clusters.remove(cluster2)
    return (cluster1, cluster2)
    
def cluster(points, n):
    clusters = [[point] for point in points]
    distances = {}
    while n != len(clusters):
        update_distances(clusters, distances)
        cluster1, cluster2 = pop_minimal_distance_pair(clusters, distances)
        new_cluster = merge_clusters(cluster1, cluster2)
        clusters.append(new_cluster)
        distances = clear_unactual_distances(distances, cluster1, cluster2)
    return sorted(clusters)

