def even_numbers(arr, n):
    even = []
    for number in arr[::-1]:
        if number % 2 == 0:
            even.append(number)
            if len(even) == n:
                break
    return even[::-1]
