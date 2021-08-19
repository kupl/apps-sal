def countsumzero(lst):
    prefixsums = [0]
    for x in lst:
        prefixsums.append(prefixsums[-1] + x)
    freq = {}
    for y in prefixsums:
        if y in freq:
            freq[y] += 1
        else:
            freq[y] = 1
    return sum((v * (v - 1) // 2 for v in list(freq.values())))


n = int(input())
a = list(map(int, input().split()))
print(countsumzero(a))
