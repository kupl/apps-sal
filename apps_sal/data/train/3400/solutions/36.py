def even_numbers(arr,n):
    out = []
    count = 0
    for el in arr[::-1]:
        if el % 2 == 0 and count < n:
            out.append(el)
            count += 1
    return out[::-1]

