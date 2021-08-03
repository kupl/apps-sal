def is_kiss(words):
    wo = words.split(' ')
    c = len(wo)
    for w in wo:
        if len(w) > c:
            return "Keep It Simple Stupid"
    return "Good work Joe!"
