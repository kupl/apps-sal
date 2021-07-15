def pac_man(N, PM, enemies):
    if not enemies:
        return N ** 2 - 1
    rows = []
    columns = []

    for i, c in enumerate(enemies):
        rows.append(c[0])
        columns.append(c[1])
    rows = sorted(rows)
    columns = sorted(columns)
    PM = list(map(lambda x: x + 1, PM))
    rows = list(map(lambda x: x + 1, rows))
    columns = list(map(lambda x: x + 1, columns))
    rows_less = list(filter(lambda a: a < PM[0], rows))
    rows_more = list(filter(lambda a: a > PM[0], rows))
    columns_less = list(filter(lambda a: a < PM[1], columns))
    columns_more = list(filter(lambda a: a > PM[1], columns))
    list(rows_more)
    if not rows_more:
        rows_more.append(N + 1)
    if not rows_less:
        rows_less.append(0)
    if not columns_more:
        columns_more.append(N + 1)
    if not columns_less:
        columns_less.append(0)
    y = min(rows_more) - max(rows_less) - 1
    x = min(columns_more) - max(columns_less) - 1

    return x*y - 1
