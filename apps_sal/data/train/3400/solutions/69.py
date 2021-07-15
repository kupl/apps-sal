def even_numbers(arr: list,n: int):
    arr.reverse()
    arr = [i for i in arr if not i % 2]
    arr = arr[:n]
    arr.reverse()
    return arr
