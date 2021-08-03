def is_solved(board):
    flat_list = []
    for item in board:
        flat_list.extend(item)
    sorted_flat_list = sorted(flat_list)
    if sorted_flat_list == flat_list:
        return True
    else:
        return False
