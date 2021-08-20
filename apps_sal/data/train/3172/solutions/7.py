def parse_fen(string):
    ranks = string.split('/')
    game_info_fields = ranks[7].split(' ')
    ranks[7] = game_info_fields[0]
    color = game_info_fields[1]
    pretty_pieces = {'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙', 'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟'}
    squares = ['▇', '＿']
    board = [[squares[(i + j) % 2] for i in range(0, 8)] for j in range(0, 8)]
    for row in range(0, 8):
        rank = ranks[row]
        column = 0
        for char in rank:
            if char.isnumeric():
                column += int(char)
            else:
                board[row][column] = pretty_pieces[char]
                column += 1
    stringify = '\n'.join([''.join(board[i]) for i in range(0, 8)])
    return stringify + '\n' if color is 'w' else stringify[::-1] + '\n'
