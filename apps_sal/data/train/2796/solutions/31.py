def areYouPlayingBanjo(name):
    status = "plays" if name[0] in "Rr" else "does not play"
    return "{n} {st} banjo".format(n=name, st=status)
