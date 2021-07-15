def summary_ranges(nums):
    def f():
        cur = []
        for x in nums:
            if not cur:
                cur = [x]
            elif x == cur[-1] + 1:
                cur[1:] = x,
            elif x != cur[-1]:
                yield cur
                cur = [x]
        if cur:
            yield cur
    return [str(xs[0]) if xs[0] == xs[-1] else f'{xs[0]}->{xs[-1]}' for xs in f()]
