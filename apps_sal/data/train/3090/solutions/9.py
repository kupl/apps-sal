
def filter_int(arr):
    res = []
    for i in arr:
        if type(i) == int:
            res.append(i)
        else:
            continue
    return res


def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def is_diff(arr):
    count = 0
    res = None
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            count += 1
            res = True
            break
        else:
            res = False
    return res


def sec_big(a, b):
    if a > b:
        return b
    else:
        return a


def find_2nd_largest(arr):
    filtered_list = filter_int(arr)
    sorted_list = sort(filtered_list)
    if is_diff(sorted_list) == True:
        a = sorted_list[len(sorted_list) - 1]
        b = sorted_list[len(sorted_list) - 2]
        sec_largest_elem = sec_big(a, b)
        return sec_largest_elem
    else:
        return None
