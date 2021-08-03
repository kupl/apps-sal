from scipy.spatial.distance import euclidean


def dropzone(p, dropzones):
    return min(dropzones, key=lambda a: euclidean(a, p))
