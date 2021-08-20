def swap_head_tail(arr):
    print(arr)
    list_arr = [*arr[int(len(arr) / 2):], *arr[:int(len(arr) / 2)]]
    list1 = arr[int(len(arr) / 2 + 1):]
    list2 = arr[:int(len(arr) / 2)]
    middle = [arr[int(len(arr) / 2)]]
    return list_arr if len(arr) % 2 == 0 else [*list1, *middle, *list2]
