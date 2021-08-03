def sum_consecutives(s, i=0):
    ret, s = [], s + ['']
    while i < len(s) - 1:
        x = sims(s, i, s[i])
        ret.append(x[0])
        i = x[1]
    return ret


def sims(arr, i, sm):
    while arr[i] == arr[i + 1]:
        i += 1
        sm += arr[i]
    return sm, i + 1
