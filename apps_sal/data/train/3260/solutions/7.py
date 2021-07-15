from itertools import permutations

def rearranger(k, *args):
    res = set([(int(''.join(map(str, p))), p) for p in permutations(args) if int(''.join(map(str, p))) % k == 0])
    if res:
        res = sorted(res)
        ans = []
        min_val = res[0][0]
        for i, p in res:
            if i != min_val:
                break
            ans.append(f'{", ".join(map(str, p))}')
        return f'Rearrangement{"s" if len(ans) > 1 else ""}: {" and ".join(ans)} {" " if len(ans) > 1 else ""}generates: {min_val} divisible by {k}'
    return 'There is no possible rearrangement'
