combinationTotals = []


def choose_best_sum(t, k, ls):
    combinationTotals.clear()
    # your code
    ls.sort()
    total = 0

    if k > len(ls) or sum(ls[:k]) > t:
        return None

    combine_segments(k, ls, [], t)
    combinationTotals.sort()
    return combinationTotals[-1]


def combine_segments(k, ls, arr, t):
    for i in range(len(ls) - k + 1):

        arr.append(ls[i])

        if k == 1:
            total = sum(arr)
            if total < t:
                combinationTotals.append(total)
            elif total == t:
                print(arr)
                combinationTotals.append(total)
                return t
            else:
                arr.pop()
                break
        else:
            if(combine_segments(k - 1, ls[i + 1:], arr, t) != None):
                return t

        arr.pop()

    return None
