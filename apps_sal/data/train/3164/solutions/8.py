def group_by_commas(n):
    rev = str(n)[::-1]
    groups = [rev[i:i + 3] for i in range(0, len(rev), 3)]
    return ','.join(groups)[::-1]
