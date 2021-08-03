def solution(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b + 1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a + 1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)
