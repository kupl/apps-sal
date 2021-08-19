def tv_remote(word):
    keyboard = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    total = 0
    r_start = 0
    c_start = 0
    for i in word:
        for j in range(len(keyboard)):
            if i.lower() in keyboard[j]:
                total += abs(j - r_start) + abs(keyboard[j].index(i.lower()) - c_start) + 1
                r_start = j
                c_start = keyboard[j].index(i.lower())
    return total
