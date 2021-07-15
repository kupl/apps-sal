import string
import numpy as np

def remove_dups(list_in):

    no_dups_t = list(set([tuple(d) for d in list_in]))
    no_dups = [list(d) for d in no_dups_t]

    return no_dups

def init_board(size):
    cols = [s for s in string.ascii_lowercase]

    board = []
    for i in range(1,size+1):
        row = str(size+1-i)
        board.append([col+row for col in cols[0:size]])

    return np.array(board)

def position_to_xy(board, position):
    position = position.replace('0','10')
    return [np.where(board == position)[0][0], np.where(board == position)[1][0]]

def xy_to_position(xy_list, size):
    out = []
    board = init_board(size)
    for xy in xy_list:
        out.append(board[xy[0]][xy[1]])

    return out

def xy_to_string(input_list):
    out = str()
    for f in input_list:
        out = out + (str(f)+',')
    out = out[0:-1]
    out = out.replace('10','0')

    return out

def init_free_fields(size):
    rows  = [i for i in range(0,size)]
    cols  = [i for i in range(0,size)]
    free_fields = [[i,j] for i in rows for j in cols]

    return free_fields

def find_blocked_fields(queen, size):

    # init
    attack = []
    x_arr = []
    y_arr = []

    y_arr.append([i for i in range(queen[0]+1, size)])
    y_arr.append([i for i in range(queen[0]+1, size)])
    y_arr.append([i for i in reversed(list(range(queen[0])))])
    y_arr.append([i for i in reversed(list(range(queen[0])))])

    x_arr = []
    x_arr.append([i for i in range(queen[1]+1, size)])
    x_arr.append([i for i in reversed(list(range(queen[1])))])
    x_arr.append([i for i in range(queen[1]+1, size)])
    x_arr.append([i for i in reversed(list(range(queen[1])))])

    # diagonal fields
    for i in range(0,4):
        min_len = min(len(y_arr[i]),len(x_arr[i]))
        for j,k in zip(y_arr[i][0:min_len], x_arr[i][0:min_len]):
            if [j,k] not in attack:
                attack.append([j,k])
            else:
                pass

    # horizontal and vertical fields
    for i in range(0, size):
        if [queen[0],i] not in attack:
            attack.append([queen[0],i])
        if [i,queen[1]] not in attack:
            attack.append([i,queen[1]])

    if queen in attack:
        attack.remove(queen)

    return attack

def remove_from_list(remove_list, from_list):

    for r in remove_list:
        if r in from_list:
            from_list.remove(r)

def update_board(size, solution):
    free_fields = init_free_fields(size)
    blocked_fields = []

    for s in solution:
        blocked_fields.extend(find_blocked_fields(s, size))

    blocked_fields = remove_dups(blocked_fields)
    remove_from_list(remove_list=solution, from_list=free_fields)
    remove_from_list(remove_list=blocked_fields, from_list=free_fields)

    return [free_fields, blocked_fields]

def place_queen(size, queen, solution):

    # check if queen´s row is already part of solution
    check_row = False
    for s in solution:
        if s[0] == queen[0]:
            check_row = True
            break

    # replace solution from row on with new queen and update solution
    if check_row == True:
        for i,s in enumerate(solution):
            if s[0] == queen[0]:
                solution = solution[0:i]
                solution.append(queen)
            else:
                pass
    else:
        solution.append(queen)

    # update board
    board = update_board(size, solution)
    free_fields = board[0]
    blocked_fields = board[1]

    # move to next row
    rows = [r for r in range(0, size) if r not in [s[0] for s in solution]]
    next_row = [[min(rows),f[1]] for f in free_fields if f[0] == min(rows)]

    if len(next_row)>0:
        for p in next_row:
            if len(solution)==size:
                break
            else:
                solution = place_queen(size, p, solution)
    else:
        return solution

    return solution

def queens(position,size):

    # init
    board = init_board(size)
    queen = position_to_xy(board, position)

    solution = []
    solution = place_queen(size, queen, solution)
    xy = xy_to_position(solution, size)

    out = xy_to_string(xy)

    return out

