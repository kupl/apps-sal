def pairs(ar, count=0):
    for c in range(len(ar) - 1):
        if c % 2 == 0 and (ar[c + 1] == ar[c] + 1 or ar[c + 1] == ar[c] - 1):
            count += 1
    return count
