def is_centered(arr, n):
    if (len(arr) % 2 == 0) and n == 0:
        return True
    left, right = (len(arr) // 2, len(arr) // 2) if len(arr) % 2 else (len(arr) // 2 - 1, len(arr) // 2)
    while left >= 0 and right <= len(arr):
        if sum(arr[left:right + 1]) == n:
            return True
        left -= 1
        right += 1
    return False
