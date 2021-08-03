def even_numbers(arr, n):
    last_n_even_numbers = list()
    for num in arr[::-1]:
        if not num % 2:
            last_n_even_numbers.append(num)
            if len(last_n_even_numbers) == n:
                return last_n_even_numbers[::-1]
