def any_arrows(arrows):
    l = list(filter(lambda x: x.get('damaged'), arrows)) 
    return len(l)<len(arrows)
