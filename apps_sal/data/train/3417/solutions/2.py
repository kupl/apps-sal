def cut_the_ropes(a):
    if not a:
        return []
    m = min(a)
    return [len(a)] + cut_the_ropes([x - m for x in a if x > m])
