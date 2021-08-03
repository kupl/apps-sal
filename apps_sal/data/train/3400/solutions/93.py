def even_numbers(arr, n):
    lst = []
    for i in arr:
        if i % 2 == 0:
            lst.append(i)
    print(lst)
    lst.reverse()
    print(lst)
    lst = lst[0:n]
    print(lst)
    lst.reverse()
    return lst
