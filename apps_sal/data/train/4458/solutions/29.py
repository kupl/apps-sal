from re import match


def time_correct(t):
    if not t:
        return t

    if not match("^\d{2}\:\d{2}\:\d{2}$", t):
        return None

    arr = [int(s) for s in t.split(':')]

    for i in range(2, 0, -1):
        if arr[i] > 59:
            arr[i - 1] += arr[i] // 60
            arr[i] = arr[i] % 60

    arr[0] = arr[0] % 24
    return ':'.join(str(num).zfill(2) for num in arr)
