def find_spec_partition(n, k, com):
    part = [0] * k
    if com == 'min':
        part[1:k] = [1] * (k - 1)
        part[0] = n - k + 1
    else:
        for p in range(len(part)):
            maxPart = round(n / (k - p))
            part[p] = maxPart
            n -= maxPart
    part.sort(reverse=True)
    return part
