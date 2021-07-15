def tv_remote(word):
    matrix = [
             ['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
             ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
             ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
             ['p', 'q', 'r', 's', 't', '.', '@', '0'],
             ['u', 'v', 'w', 'x', 'y', 'z', '_', '/'],
             ]

    start = [0, 0]
    _dict = dict()
    actions = []
    _lambda = lambda x, y: (abs(x[0]-y[0]) + abs(x[1]-y[1]))+1

    for char in word:
        for i in range(5):
            if char in matrix[i]:
                _dict[char] = [i, matrix[i].index(char)]
        actions.append(_lambda(start, _dict[char]))
        start = _dict[char]

    return sum(actions)
