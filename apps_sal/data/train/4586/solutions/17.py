def tv_remote(word):
    remote = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    prev_pos, pres = [0, 0], 0
    for symb in word:
        pos = [remote.find(symb) // 8, remote.find(symb) % 8]
        pres += abs(pos[0] - prev_pos[0]) + abs(pos[1] - prev_pos[1]) + 1
        prev_pos = pos

    return pres
