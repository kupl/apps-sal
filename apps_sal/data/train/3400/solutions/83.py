def even_numbers(arr,n):
    new_arr = []
    even = []

    for i in arr:
        if i % 2 == 0:
            new_arr.append(i)

    for j in range(n):
        even.append(new_arr[-(j+1)])
    even.reverse()
    return even
    


