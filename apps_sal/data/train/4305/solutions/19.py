def order_weight(strng):
    nums = strng.split()
    l = []
    for n in nums:
        s = sum(list(int(i) for i in n))
        l += [[s,n]]
    l.sort()
    return ' '.join([i[-1] for i in l])
