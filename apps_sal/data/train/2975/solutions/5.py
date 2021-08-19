def song_decoder(song):
    """ Simple WUB decoder :) """

    # Splitting strings by "WUBs" and filtering out voids
    list = filter(lambda x: x != '', song.split('WUB'))

    # Returning the joint items separed by spaces
    return ' '.join(list)
