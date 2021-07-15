def invite_more_women(arr):
    if len([i for i in arr if i != 1]) < len([i for i in arr if i != -1]):
        return True
    else:
        return False
