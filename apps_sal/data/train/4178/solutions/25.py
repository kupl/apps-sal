def min_sum(arr):
    return sum(sorted(arr)[i]*sorted(arr)[-i-1] for i in range(len(arr)//2))
