def find_missing_number(sq):
    if sq == '':
        return 0
    try:
        arr = [int(e) for e in sq.split(' ')]
    except ValueError:
        return 1
    else:
        arr.sort()
        for i in range(0, len(arr)):
            if arr[i] != i + 1:
                return i + 1
        return 0
