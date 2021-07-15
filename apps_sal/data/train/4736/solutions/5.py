def how_many_bees(hive):
    if hive is None:
        return 0
    columns = ["".join(col) for col in zip(*hive)]
    hive = ["".join(line) for line in hive]
    return sum(row.count(bee) for bee in ("bee", "eeb") for rows in (hive, columns) for row in rows)
