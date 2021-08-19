def tv_remote(word):
    remote = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    position = [0, 0]
    pressings = 0

    def find_key(key):
        for i in range(len(remote)):
            if key in remote[i]:
                return [i, remote[i].find(key)]
    for letter in word:
        pressings += 1 + abs(find_key(letter)[0] - position[0]) + abs(find_key(letter)[1] - position[1])
        position = find_key(letter)
    return pressings
