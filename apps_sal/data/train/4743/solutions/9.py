memo={}
def target_game(values):
    if len(values)==1:
        return max(values[0],0)
    elif len(values)==2:
        return max(values[0],values[1],0)
    elif len(values)==3:
        return max(max(values[0],values[2],values[0]+values[2],0),values[1])
    t=tuple(values)
    if t in memo:
        return memo[t]
    r=max(max(values[0],0)+target_game(values[2:]),max(values[1],0)+target_game(values[3:]))
    memo[t]=r
    return r
