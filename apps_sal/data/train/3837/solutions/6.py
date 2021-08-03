def reverse(right):
    last_row = []

    for a in right:
        curr_row = [a]
        for b in last_row:
            a = b - a
            curr_row.append(a)

        last_row = curr_row

    return last_row[::-1]
