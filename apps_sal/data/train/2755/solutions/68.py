def multiple_of_index(arr):
    ll = list()
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            ll.append(arr[i])
    return ll
