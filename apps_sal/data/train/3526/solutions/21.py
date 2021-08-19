def any_arrows(arrows):
    try:
        return not (arrows == [] or all((x['damaged'] for x in arrows)))
    except KeyError:
        return True
