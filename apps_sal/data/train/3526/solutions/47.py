def any_arrows(arr):
    for i in arr:
        if True not in i.values():
            return True
    return False
