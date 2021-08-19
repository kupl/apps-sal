buf = [45, 54, 495, 594]


def sum_dif_rev(n):
    i = buf[-1]
    while len(buf) < n:
        i += 1
        j = int(str(i)[::-1])
        d = abs(i - j)
        if i % 10 and d and (not (i + j) % d):
            buf.append(i)
    return buf[n - 1]
