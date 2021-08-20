def comfortable_numbers(l, r):
    sm = 0
    dig = [sum((int(x) for x in str(i))) for i in range(l, r + 1)]
    for i in range(l, r):
        for j in range(i + 1, i + dig[i - l] + 1):
            if j > r:
                break
            if j - i <= dig[j - l]:
                sm += 1
    return sm
