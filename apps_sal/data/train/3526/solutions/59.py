def any_arrows(arrows):
    quiver = False
    if arrows:
        for n, x in enumerate(arrows):
            for k, v in x.items():
                if k == 'range' and len(x.items()) == 1:
                    quiver = True
                    break
                if k == 'damaged' and v == False:
                    quiver = True
                    break
    return quiver
