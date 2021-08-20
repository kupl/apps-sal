def solve(arr):
    nums = set()
    out = []
    for elem in reversed(arr):
        if elem not in nums:
            out.append(elem)
            nums.add(elem)
    return out[::-1]
