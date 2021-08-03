def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


def get_positions(n):
    return tuple(int(d) for d in ternary(n)[-3:].zfill(3)[::-1])
