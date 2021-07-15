def even_numbers(arr,n):
    list = []
    for number in reversed(arr):
        if number % 2 == 0:
            list.append(number)
        if len(list) == n:
            return list[::-1]

