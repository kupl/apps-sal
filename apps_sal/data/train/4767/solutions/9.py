from itertools import combinations


def longest_comb(arr, command):
    (inc, mx, res) = (command.replace(' ', '') == '<<', 0, [])
    for k in range(len(arr), 2, -1):
        if k < mx:
            break
        for comb in combinations(arr, k):
            if inc and all((a < b for (a, b) in zip(comb, comb[1:]))) or (not inc and all((a > b for (a, b) in zip(comb, comb[1:])))):
                if k > mx:
                    res = [list(comb)]
                    mx = k
                elif k == mx:
                    res.append(list(comb))
    return res[0] if len(res) == 1 else res
