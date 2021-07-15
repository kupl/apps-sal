def summary_ranges(nums):
    l, index = [[]], 0
    for x in nums:
        if not l[index] or (l[index][-1] + 1) == x:
            l[index].append(x)
        else:
            if l[index] != [x]:
                l.append([x])
                index += 1
    return [] if not nums else [str(x[0]) if len(x)<2 else f"{x[0]}->{x[-1]}" for x in l]
