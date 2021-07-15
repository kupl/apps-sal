def find_even_index(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i+1:])]
    return r[0] if r else -1
