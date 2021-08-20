def remove_chars(s):
    import re
    return re.sub('[^a-zA-Z\\s]', '', s)
