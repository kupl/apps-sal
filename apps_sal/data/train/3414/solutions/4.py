from itertools import cycle


def reversi_row(moves):
    row = ['.'] * 8
    player = cycle('*O')
    for move in moves:
        current_player = next(player)
        invalid = {'.', current_player}
        row[move] = current_player
        row_str = ''.join(row)
        first_left = row_str.rfind(current_player, 0, move)
        if first_left != -1:
            left_chunk = row_str[first_left + 1:move]
            if not invalid.intersection(left_chunk):
                row[first_left + 1:move] = [current_player] * len(left_chunk)
        first_right = row_str.find(current_player, move + 1)
        if first_right != -1:
            right_chunk = row_str[move + 1:first_right]
            if not invalid.intersection(right_chunk):
                row[move + 1:first_right] = [current_player] * len(right_chunk)
    return ''.join(row)
