def multiple_of_index(arr):
    return [arr[el] for el in range(1, len(arr)) if arr[el] % el == 0]

