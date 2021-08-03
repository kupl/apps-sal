def invite_more_women(arr):
    add_vec = 0
    for i in range(0, len(arr)):
        add_vec += arr[i]
    if add_vec <= 0:
        return False
    else:
        return True
