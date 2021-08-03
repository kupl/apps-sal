def dont_give_me_five(start, end):
    arr = []
    for x in range(start, end + 1):
        if "5" not in str(x):
            arr.append(x)
    return len(arr)
