def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()
