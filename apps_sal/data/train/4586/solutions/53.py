def tv_remote(word):
    remote = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'],  # 0, 3 = 3
              ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],  # 2, 4 = 6
              ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],  # 0, 4 = 4
              ['p', 'q', 'r', 's', 't', '.', '@', '0'],  # 3, 3 = 6
              ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    x, y = 0, 0
    enter = 1
    moves = 0
    for char in word:
        for row in range(len(remote)):
            for column in range(8):
                if remote[row][column] == char:
                    moves += abs(x - row) + abs(y - column) + enter
                    x = row
                    y = column
    return moves
