def even_numbers(arr,n):
    even_numbers_in_arr = []
    new_even_numbers = []
    for number in arr:
        if number % 2 == 0:
            even_numbers_in_arr.append(number)
    even_numbers_in_arr.reverse()
    for i in range(n):
        new_even_numbers.append(even_numbers_in_arr[i])
    new_even_numbers.reverse()
    return new_even_numbers

