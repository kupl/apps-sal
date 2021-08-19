import math
import numpy as np
import itertools


def cluster(points, n):

    def get_cluster_distance(cluster1, cluster2):

        # function to find distance between a single pair
        def get_point_distance(coord_1, coord_2):
            x1, y1 = coord_1
            x2, y2 = coord_2
            return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

        distances = []
        for point_i in cluster1:
            for point_j in cluster2:
                distances.append(get_point_distance(point_i, point_j))

        return np.mean(distances)

    # Initiate list of all clusters, initially every point is a cluster (its own list)
    all_clusters = [[point] for point in points]

    # Main function
    while len(all_clusters) > n:
        distances = []
        for i, j in itertools.combinations([_ for _ in range(len(all_clusters))], 2):
            distances.append([i, j, get_cluster_distance(all_clusters[i], all_clusters[j])])
        minimum_distance_pair = min(distances, key=lambda x: x[2])
        i, j, distance = minimum_distance_pair
        all_clusters[i] = all_clusters[i] + all_clusters.pop(j)

    # Sort points in each cluster
    for i in range(len(all_clusters)):
        all_clusters[i] = sorted(all_clusters[i])
    # Sort each cluster
    return sorted(all_clusters)
