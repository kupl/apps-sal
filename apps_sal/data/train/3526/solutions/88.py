def any_arrows(a):
    for i in range(len(a)):
        if a[i].get('damaged') != True:
            return True
    return False
