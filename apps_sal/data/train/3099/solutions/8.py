import re

def check(line, ch, connect):
    return re.search(re.escape(ch)+'{'+re.escape(str(connect))+'}', ''.join(line))

def decide(matrix, i, j, connect, size):
        ch = matrix[i][j]
        row = matrix[i][max(0, j - connect + 1):j + connect]
        if check(row, ch, connect) : return True
    
        column = [k[j] for k in matrix[max(0, i - connect + 1):i + connect]]
        if check(column, ch, connect) : return True
    
        for x in [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]:
            diagonal = []
            for ind, (k, l) in enumerate(x):
                ni, nj, li = i + k, j + l, []
                while 0 <= ni < size and 0 <= nj < size and len(li) != connect and matrix[ni][nj] != ' ':
                    li.append(matrix[ni][nj])
                    ni += k
                    nj += l
                diagonal.extend(li[::[-1,1][ind]] + [ch])
            if check(diagonal[:-1], ch, connect) : return True
        return False

def whoIsWinner(moves,connect,size):
    matrix = [[' ' for _ in range(size)] for _ in range(size)]
    columns = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[:size]
    AVL = {i: size - 1 for i in columns}

    for move in moves:
        col, player = move.split('_')
        r, c = AVL[col], columns.index(col)
    
        matrix[r][c] = player
        AVL[col] -= 1

        if decide(matrix, r, c, connect, size) : return player
    return 'Draw'
