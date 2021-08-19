def array_leaders(n):
    leaders = []
    for i in range(len(n) - 1, -1, -1):
        if n[i] > sum(n[i + 1:]):
            leaders.append(n[i])
    leaders.reverse()
    return leaders
