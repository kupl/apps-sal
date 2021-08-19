def artificial_rain(li):
    (left, m, i) = (0, 0, 1)
    while i < len(li):
        prev = left
        while i < len(li) and li[i - 1] <= li[i]:
            if li[left] != li[i]:
                left = i
            i += 1
        while i < len(li) and li[i - 1] >= li[i]:
            if li[left] != li[i]:
                left = i
            i += 1
        m = max(m, i - prev)
    return m or 1
