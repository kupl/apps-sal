import re


def areYouPlayingBanjo(name):
    return name + ' plays banjo' if re.search('\\A[rR]', name) else name + ' does not play banjo'
