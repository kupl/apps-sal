def any_arrows(arrows):
    return any([not arr["damaged"] if "damaged" in arr.keys() else True for arr in arrows])
