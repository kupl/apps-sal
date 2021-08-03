def comfortable_numbers(l, r):
    used = {l}
    s = {l: sum(int(i) for i in str(l))}
    count = 0

    for a in range(l, r):
        sa = s[a]
        for b in range(a + 1, r + 1):
            if b in used:
                sb = s[b]
            else:
                sb = sum(int(i) for i in str(b))
                s.update({b: sb})
                used.add(b)
            if a - sa <= b <= a + sa and b - sb <= a <= b + sb:
                count += 1

    return count
