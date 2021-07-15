def unorderedPartitions(targetNum, targetSize, minNum = 1):
    if targetSize == 1:
        return [[targetNum]]
    partitions = []
    for partNum in range(minNum, targetNum // targetSize + 1):
        partitions += [[partNum] + part for part in unorderedPartitions(targetNum - partNum, targetSize - 1, partNum + 1)]
        return partitions # return first found partition only

def solve(n, k):
    factors = set()
    for f in range(1, int(n ** 0.5) + 1):
        if n % f == 0:
            factors.add(f)
            factors.add(n // f)
    factors = sorted(factors, reverse = True)
    # minimum sum of (n // gcd)
    minSum = k * (k + 1) // 2
    for factor in factors:
        if factor * minSum > n:
            continue
        partition = unorderedPartitions(n // factor, k)[0]
        if len(partition) == len(set(partition)):
            return [x * factor for x in partition]
    return []
