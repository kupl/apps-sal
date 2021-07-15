def any_arrows(arrows):
    damaged_arrows = 0
    total_arrows = 0
    for x in arrows:
        if 'damaged' in x:
            if x['damaged']:
                damaged_arrows += 1
        total_arrows += 1
    return total_arrows > damaged_arrows

