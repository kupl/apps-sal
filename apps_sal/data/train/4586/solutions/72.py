def tv_remote(word):
    kboard = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', 'f', 'g', 'h', 'i', 'j', '4', '5', '6', 'k', 'l', 'm', 'n', 'o', '7', '8', '9', 'p', 'q', 'r', 's', 't', '.', '@', '0', 'u', 'v', 'w', 'x', 'y', 'z', '_', '/']
    start = 'a'
    count = 0
    for c in word:
        pos1 = kboard.index(start)
        pos2 = kboard.index(c)
        count += max(pos1 // 8, pos2 // 8) - min(pos1 // 8, pos2 // 8)
        count += max(pos1 % 8, pos2 % 8) - min(pos1 % 8, pos2 % 8)
        count += 1
        start = c
    return count
