def group_by_commas(n):
    # reverse number as string
    rev = str(n)[::-1]
    # break into groups of 3
    groups = [rev[i:i + 3] for i in range(0, len(rev), 3)]
    # insert commas and reverse it
    return ','.join(groups)[::-1]
