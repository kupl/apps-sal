from sklearn.cluster import KMeans
from collections import defaultdict


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def MeanDist(clus1, clus2):
    c = 0
    for p1 in clus1:
        for p2 in clus2:
            c += dist(p1, p2)
    return c / (len(clus1) * len(clus2))


def cluster(points, n):
    if len(points) < 20:
        pred = KMeans(n_clusters=n).fit_predict(points)
        ans = defaultdict(list)
        for x, y in zip(pred, points):
            ans[x].append(y)
        res = [sorted(i) for i in list(ans.values())]
        res = sorted(res, key=lambda x: x[0][0])
        return res

    clus = [[p] for p in points]
    leng = len(clus)
    while leng > n:
        md = float('inf')
        for i in range(leng):
            for j in range(i + 1, leng):
                d = MeanDist(clus[i], clus[j])
                if d < md:
                    md = d
                    c = [clus[i] + clus[j]]
                    curr = [i, j]
        temp = [x for i, x in enumerate(clus) if i not in curr]
        clus = temp + c
        leng = len(clus)
    res = [sorted(i) for i in clus]
    res = sorted(res, key=lambda x: x[0][0])
    return res
