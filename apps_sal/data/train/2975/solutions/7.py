def song_decoder(song):
    if 'WUB' not in song:
        return song
    else: 
        return ' '.join(song.replace('WUB',' ').split())
