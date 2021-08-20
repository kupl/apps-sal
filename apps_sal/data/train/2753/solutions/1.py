def is_kiss(words):
    words = words.split(' ')
    return 'Keep It Simple Stupid' if any((len(word) > len(words) for word in words)) else 'Good work Joe!'
