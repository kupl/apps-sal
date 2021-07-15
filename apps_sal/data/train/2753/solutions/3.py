def is_kiss(s):
    words = s.split()
    return 'Good work Joe!' if all(len(word) <= len(words) for word in words) else 'Keep It Simple Stupid'
