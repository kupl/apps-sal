DIRS = {'Left': 'Right', 'Right': 'Left'}


def solve(arr):
    lst, prevDir = [], 'Begin'
    for cmd in arr[::-1]:
        d, r = cmd.split(' on ')
        follow = DIRS.get(prevDir, prevDir)
        prevDir = d
        lst.append(f'{follow} on {r}')
    return lst
