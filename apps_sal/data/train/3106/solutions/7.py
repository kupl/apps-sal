def combs_non_empty_boxes(n, k):
    if n < k:
        return 'It cannot be possible!'
    else:
        row = [1] + [0 for x in range(k)]
        for i in range(1, n + 1):
            new = [0]
            for j in range(1, k + 1):
                stirling = j * row[j] + row[j - 1]
                new.append(stirling)
            row = new
        return row[k]
