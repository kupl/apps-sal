def dist_between_clusters(cluster1, cluster2):
    res = 0
    n = 0
    for point1 in cluster1:
        for point2 in cluster2:
            res += ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2) ** 0.5
            n += 1
    return res / n

def cluster(points, n):
    clusters = [[point] for point in points]
    
    while n < len(clusters):
        min_dist, min1, min2 = None, None, None
        for i, cluster1 in enumerate(clusters[:-1]):
            for j, cluster2 in enumerate(clusters[i+1:]):
                dist = dist_between_clusters(cluster1, cluster2)
                if min_dist is None or dist < min_dist:
                    min_dist, min1, min2 = dist, i, i+1+j
        clusters[min1].extend(clusters[min2])
        clusters.pop(min2)
    
    for i in range(len(clusters)):
        clusters[i].sort()
    clusters.sort()
    
    return clusters

