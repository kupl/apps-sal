def circularly_sorted(arr):
    N, jump = len(arr), False
    for i, n in enumerate(arr):
        if n > arr[(i + 1) % N]:
            if jump:
                return False
            jump = True
    return True
