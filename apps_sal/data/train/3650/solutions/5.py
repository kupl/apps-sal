def solve(arr):
    links = {}
    for a in arr:
        if a % 3 == 0:
            next_val = a // 3
            if next_val in arr:
                links[a] = next_val
        if a * 2 in arr:
            links[a] = a * 2

    start = (set(links.keys()) - set(links.values())).pop()
    result = [start]
    while True:
        next_val = links.get(result[-1])
        if next_val is None:
            break
        result.append(next_val)
    return result
