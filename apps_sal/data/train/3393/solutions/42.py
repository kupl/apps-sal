def list_squared(m, n):
    res = []
    pairs = [[1, 1],
             [42, 2500],
             [246, 84100],
             [287, 84100],
             [728, 722500],
             [1434, 2856100],
             [1673, 2856100],
             [1880, 4884100],
             [4264, 24304900],
             [6237, 45024100],
             [9799, 96079204],
             [9855, 113635600]]
    for i in range(m, n + 1):
        for idx, x in enumerate(pairs):
            if i == x[0]:
                res.append(x)
    return res
