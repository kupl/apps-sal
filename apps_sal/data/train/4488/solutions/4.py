def bucketize(*arr):
    bucket = (1+len(arr)) * [None]
    for x in sorted(set(arr)):
        l = bucket[arr.count(x)]
        if l is None:
            bucket[arr.count(x)] = []
        bucket[arr.count(x)].append(x)
    return bucket
