def song_decoder(song):
    return ' '.join(list(filter(('').__ne__, song.split('WUB'))))
