def song_decoder(song):
    original = ''
    cut = 0
    while song != '':
        if song[:3] != 'WUB':
            if cut == 1:
                original += ' '
            original += song[0]
            song = song[1:]
            cut = 0
        else:
            song = song[3:]
            cut = 1
    return original.strip()
