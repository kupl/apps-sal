def tv_remote(word):
    string = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    mydict = {letter: dict() for letter in string}
    visited = set()

    for i in range(5):
        for j in range(8):

            board = [list(string[x * 8:x * 8 + 8]) for x in range(5)]
            base = board[i][j]
            queue = [(i, j, 0)]
            while queue:

                x, y, dist = queue.pop(0)
                if board[x][y] in visited:
                    continue
                if board[x][y] == -1:
                    continue

                letter = board[x][y]
                board[x][y] = -1

                mydict[base][letter] = dist
                mydict[letter][base] = dist

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                        queue.append((x + dx, y + dy, dist + 1))

            visited.add(base)

    base = 'a'
    nums = 0
    for letter in word:
        nums += mydict[base][letter]
        base = letter

    return nums + len(word)
