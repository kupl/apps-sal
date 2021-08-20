def solve(arr):
    values = set()
    removed_values = set()
    for value in arr:
        if value in removed_values:
            continue
        opposite = value * -1
        if opposite in values:
            values.remove(opposite)
            removed_values.add(value)
            removed_values.add(opposite)
        else:
            values.add(value)
    return list(values)[0]
