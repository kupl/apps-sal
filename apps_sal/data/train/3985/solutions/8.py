find_even_index = lambda arr: next((i for i, __ in enumerate(arr) if sum(arr[:i]) == sum(arr[i+1:])), -1)
