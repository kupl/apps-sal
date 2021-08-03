def any_arrows(arrows):
    return sum(1 if 'damaged' not in list(each.keys()) or ('damaged' in list(each.keys()) and not each['damaged']) else 0 for each in arrows) > 0
