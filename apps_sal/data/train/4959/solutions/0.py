def find_ball(scales, n):
    select = list(range(n))
    while len(select) > 1:
        left, right, unused = select[::3], select[1::3], select[2::3]
        if len(select) % 3 == 1:
            unused.append(left.pop())
        select = [left, unused, right][scales.get_weight(left, right) + 1]
    return select.pop()
