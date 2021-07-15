def word_pattern(pattern, string):
    
    words = string.split(' ')
    
    if len(words) != len(pattern):
        return False
    
    map, used = {}, set()
    
    for i, p in enumerate(pattern):
        
        w = words[i]

        if p not in map and w not in used:
            map[p] = w
            used.add(w)
        
        if map.get(p, None) != w:
            return False

    return True
