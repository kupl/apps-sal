def any_arrows (arrows):
    return not all (arrow.get ('damaged', False) for arrow in arrows)
