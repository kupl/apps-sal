def any_arrows(arrows):
   return any(not arrows[i].get('damaged',False) for i in range(len(arrows)))
