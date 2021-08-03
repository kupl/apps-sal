def tidyNumber(n):
    x = str(n)
    arr = list(x)
    if len(x) == 1:
        return True
    else:
        for j in range(0, len(x) - 1):
            if arr[j] > arr[j + 1]:
                return False
        return True
