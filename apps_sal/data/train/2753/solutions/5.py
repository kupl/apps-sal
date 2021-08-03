def is_kiss(words):
    return "Keep It Simple Stupid" if max(len(i) for i in words.split()) > len(words.split()) else "Good work Joe!"
