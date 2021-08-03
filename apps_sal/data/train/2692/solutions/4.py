def bubble(l):
    snapshots = []
    for i in range(len(l), 1, -1):
        for j in range(1, i):
            if l[j - 1] > l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]
                snapshots.append(l[:])
    return snapshots
