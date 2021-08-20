def areYouPlayingBanjo(n):
    return n + [' does not play banjo', ' plays banjo'][n[0].lower() == 'r']
