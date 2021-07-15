def dont_give_me_five(start, end):
    arr = []
    for i in range(start, end + 1):
        arr.append(i)
    count = 0
    for i in arr:
        if "5" in str(i):
            count += 1
    return len(arr) - count
