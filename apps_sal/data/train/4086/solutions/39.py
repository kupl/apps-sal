def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l) + 1))


def first_non_consecutive(nums):
    if checkConsecutive(nums):
        return None
    else:
        gaps = [[s, e] for (s, e) in zip(nums, nums[1:]) if s + 1 < e]
        edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
        A = list(zip(edges, edges))
        A.pop(0)
        L = []
        for i in A:
            for j in i:
                L.append(j)
        return L[0]
