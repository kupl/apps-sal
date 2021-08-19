def is_kiss(stg):
    words = stg.split()
    l = len(words)
    return 'Good work Joe!' if all((len(word) <= l for word in words)) else 'Keep It Simple Stupid'
