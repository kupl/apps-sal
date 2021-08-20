score = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]


def getCoordinate(letter):
    x = [l.index(letter) for l in score if letter in l]
    y = [c for c in range(len(score)) if letter in score[c]]
    return [x[0], y[0]]


def tv_remote(word):
    res = 0
    pos = [0, 0]
    for let in word:
        newPos = getCoordinate(let)
        res += abs(pos[0] - newPos[0]) + abs(pos[1] - newPos[1]) + 1
        pos[0] = newPos[0]
        pos[1] = newPos[1]
    return res
