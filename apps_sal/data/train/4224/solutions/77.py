def dont_give_me_five(start, end):
    arr = []
    ran = []

    for i in range(start, end + 1):
        ran.append(i)

    for i in ran:
        s = str(i)
        if '5' in s:
            continue
        else:
            arr.append(s)

    n = len(arr)

    return n
