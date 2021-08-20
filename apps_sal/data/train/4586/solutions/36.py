def tv_remote(word):
    c_pos = [0, 0]
    remote = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    move = len(word)
    for let in word:
        y = 0
        for key in remote:
            if let in key:
                x = key.find(let)
                move += abs(y - c_pos[0]) + abs(x - c_pos[1])
                c_pos = [y, x]
            y += 1
    return move
