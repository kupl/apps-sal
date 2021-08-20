def song_decoder(song):
    """ Simple WUB decoder :) """
    list = filter(lambda x: x != '', song.split('WUB'))
    return ' '.join(list)
