def solve(arr):
    lst,prevDir = [],None
    for cmd in arr[::-1]:
        d,r = cmd.split(' on ')
        if not lst: lst.append(f'Begin on {r}')
        else:       lst.append(f'{"Left" if prevDir == "Right" else "Right"} on {r}')
        prevDir = d
    return lst
