def is_kiss(s):
    words = s.split()
    total_words = len(words)
    if all(len(a) <= total_words for a in words):
        return 'Good work Joe!'
    return 'Keep It Simple Stupid'
