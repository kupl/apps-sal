def even_numbers(arr,n):
    lst = [num for i, num in enumerate(arr) if not num % 2]
    return [lst[i] for i in range(len(lst) - n, len(lst))]
