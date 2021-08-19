def subsetsum(nums, tgt):
    sums = {}
    for n in nums[::2]:
        for (k, v) in list(sums.items()) + [(0, [])]:
            newsum = k + n
            if newsum not in sums:
                sums[newsum] = v + [n]
                if newsum == tgt:
                    return sums[tgt]
    difs = {tgt: []}
    for n in nums[1::2]:
        for (k, v) in list(difs.items()):
            newdif = k - n
            if newdif not in difs:
                difs[newdif] = v + [n]
                if newdif in sums:
                    return sums[newdif] + difs[newdif]
    return []


(n, q) = input().split()
(n, q) = (int(n), int(q))
a = input().split()
a = [int(x) for x in a]
while q > 0:
    s = input().split()
    s = [int(x) for x in s]
    l = s[1]
    r = s[2]
    if s[0] == 1:
        a[l - 1] = r
    elif s[0] == 2:
        i = l - 1
        j = r - 1
        while i <= j:
            swap = a[i]
            a[i] = a[j]
            a[j] = swap
            i += 1
            j -= 1
    else:
        w = s[3]
        b = a[l - 1:r] + [0]
        if len(subsetsum(b, w)) > 0:
            print('Yes')
        else:
            print('No')
    q = q - 1
