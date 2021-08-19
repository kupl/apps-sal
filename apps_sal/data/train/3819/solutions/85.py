def smash(words):
    # Begin here

    sayac = len(words)
    yazi = ""

    for kelime in words:
        yazi += kelime
        sayac -= 1
        if sayac == 0:
            break

        yazi += " "

    return yazi
