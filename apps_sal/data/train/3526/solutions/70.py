def any_arrows(arrows):
    for arrow_dict in arrows:
        if 'damaged' not in arrow_dict or not arrow_dict['damaged']:
            return True
    return False
