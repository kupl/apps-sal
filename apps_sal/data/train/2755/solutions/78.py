def multiple_of_index(arr):
    return [i[1] for i in zip(list(range(1, len(arr))), arr[1:]) if i is 0 or i[1]%i[0]==0]

