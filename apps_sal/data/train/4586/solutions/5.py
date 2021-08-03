def tv_remote(word):
    # define the remote grid in a dictionary
    grid = {
        "a": [1, 1], "b": [1, 2], "c": [1, 3], "d": [1, 4], "e": [1, 5], "1": [1, 6], "2": [1, 7], "3": [1, 8],
        "f": [2, 1], "g": [2, 2], "h": [2, 3], "i": [2, 4], "j": [2, 5], "4": [2, 6], "5": [2, 7], "6": [2, 8],
        "k": [3, 1], "l": [3, 2], "m": [3, 3], "n": [3, 4], "o": [3, 5], "7": [3, 6], "8": [3, 7], "9": [3, 8],
        "p": [4, 1], "q": [4, 2], "r": [4, 3], "s": [4, 4], "t": [4, 5], ".": [4, 6], "@": [4, 7], "0": [4, 8],
        "u": [5, 1], "v": [5, 2], "w": [5, 3], "x": [5, 4], "y": [5, 5], "z": [5, 6], "_": [5, 7], "/": [5, 8]}

    total_moves = 0
    start_pos = [1, 1]

    for l in word:
        v_moves = abs(grid[l][0] - start_pos[0])
        h_moves = abs(grid[l][1] - start_pos[1])
        total_moves += (v_moves + h_moves + 1)
        start_pos = grid[l]
    return total_moves
