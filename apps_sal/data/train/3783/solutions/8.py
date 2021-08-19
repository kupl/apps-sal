def frame(text, char):
    """
        First this function will find the length of the top/bottom frames
        Next it creates the word frames
        Then it constructs the full frame
    """
    max_length = max([len(word) for word in text])
    frame_words = [char + ' ' + word + (max_length - len(word) + 1) * ' ' + char for word in text]
    frame = char * (max_length + 4) + '\n'
    for line in frame_words:
        frame = frame + line + '\n'
    return frame + char * (max_length + 4)
