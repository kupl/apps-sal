def min_and_max(l, d, x):
    arr = [i for i in range(l, d+1) if sum(map(int, str(i))) == x]
    return [arr[0],arr[-1]]

