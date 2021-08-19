def is_sorted_and_how(arr):
    list_a = []
    list_d = []
    list_a = sorted(arr)
    for i in list_a[::-1]:
        list_d.append(i)
    if arr == list_a:
        return 'yes, ascending'
    if arr == list_d:
        return 'yes, descending'
    else:
        return 'no'
