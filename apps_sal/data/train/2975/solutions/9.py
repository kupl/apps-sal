def song_decoder(song):
    while 'WUBWUB' in song:
        song = song.replace('WUBWUB', 'WUB')
    song = song.replace('WUB', ' ')
    song = song.strip()
    return song
