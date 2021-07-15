def is_kiss(words):
    words = words.split()
    for w in words:
        if len(w) > len(words):
            return "Keep It Simple Stupid"
    return "Good work Joe!"
