def song_decoder(song):
    return ' '.join(list(filter(('').__ne__, song.split('WUB'))))
    # Steps:
    # 1. Remove occurences of WUB and get a list of words.
    # 2. Filter out empty space ''.
    # 3. Join the words in the list with space.
    # 4. Return

