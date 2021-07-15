def even_numbers(arr,n):
    arr.reverse()
    output = []
    i = 0
    while len(output) < n:
        if arr[i] % 2 == 0:
            output.append(arr[i])
        i += 1
    output.reverse()
    return output
