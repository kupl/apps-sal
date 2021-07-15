def tv_remote(word):
    kb = ['abcde123','fghij456','klmno789','pqrst.@0','uvwxyz_/']
    kb_d = {}
    for i, row in enumerate(kb):
        for j, char in enumerate(row):
            kb_d[char] = (i, j)
            
    x, y = 0, 0
    counter = 0
    
    for letter in word:
        dx, dy = kb_d[letter]
        counter += abs(dx-x) + abs(dy-y) + 1
        x, y = dx, dy
    
    return counter   
