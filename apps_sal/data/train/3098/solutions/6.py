def compute_depth(n):
    digits, depth, num = set('1234567890'), 1, n

    while True:
        digits -= set(str(num))

        if not digits:
            return depth

        num += n
        depth += 1
