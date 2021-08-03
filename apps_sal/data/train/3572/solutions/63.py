def invite_more_women(arr):
    men = len([i for i in arr if i > 0])
    women = len([i for i in arr if i < 0])

    return True if men > women else False
