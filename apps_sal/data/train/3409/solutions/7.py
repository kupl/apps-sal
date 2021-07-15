from collections import Counter

def fish(shoal):
    count = Counter(map(int, shoal))
    
    size, eaten, step = 1, 0, 4
    for n in range(1, 10):
        if size >= n:
            eaten += count[n] * n
            while eaten >= step:
                eaten -= step
                size += 1
                step += 4
        else:
            break
    
    return size
