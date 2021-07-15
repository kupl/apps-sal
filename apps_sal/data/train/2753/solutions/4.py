def is_kiss(words):
    return "Keep It Simple Stupid" if any(len(i) > len(words.split()) for i in words.split()) else "Good work Joe!"
