def is_centered(arr, n):
    while True:
        if sum(arr) == n:
            return True
        try:
            (arr.pop(), arr.pop(0))
        except IndexError:
            return False
