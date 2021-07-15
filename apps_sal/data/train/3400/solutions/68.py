def even_numbers(arr,n):
    even_list = []
    for num in arr:
        if num % 2 == 0:
            even_list.append(num)
    return even_list[-n:]
        

