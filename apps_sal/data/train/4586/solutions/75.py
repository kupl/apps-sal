def tv_remote(word):
    kb = {char: (pos // 8, pos % 8) for (pos, char) in enumerate('abcde123fghij456klmno789pqrst.@0uvwxyz_/')}
    (presses, current) = (0, (0, 0))
    for char in word:
        presses += 1 + abs(current[0] - kb[char][0]) + abs(current[1] - kb[char][1])
        current = kb[char]
    return presses
