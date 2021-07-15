def even_numbers(arr, n):
    x = [k for k in arr if k % 2 == 0]
    while len(x) > n:
        for k in x:
            x.remove(k)
            break
    return x
