def replace_zero(arr):
    z = [0] + [i for i in range(len(arr)) if not arr[i]] + [len(arr)]
    sums = sorted([[sum(arr[z[i]:z[i + 2]]), z[i + 1]] for i in range(len(z) - 2)])
    return sums[-1][1]
