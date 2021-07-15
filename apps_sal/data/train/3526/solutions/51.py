def any_arrows(arrows):
    return not all('damaged' in arrow and arrow['damaged'] for arrow in arrows)
