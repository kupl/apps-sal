def solve(arr):
    cleaned = list(set(arr))
    for i in cleaned:
        if not -i in cleaned:
            return i

