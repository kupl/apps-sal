import numpy as np


def switch(argument):
    switcher = {
        'F': 0,
        'L': -1,
        'R': 1
    }
    return switcher.get(argument, '')


def resize(p_matrix, num, axis, dir):
    if axis == 1:
        right = np.zeros((p_matrix.shape[0], num))
        left = p_matrix
        if dir == 2:
            right, left = left, right
        re_matrix = np.append(left, right, axis)
    else:
        top = np.zeros((num, p_matrix.shape[1]))
        bot = p_matrix
        if dir == 1:
            top, bot = bot, top
        re_matrix = np.append(top, bot, axis)
    return re_matrix


def mk_matrix(trace):
    p_matrix = np.full((1, 1), 1)
    pos = [0, 0]
    for i in range(len(trace)):

        dir = trace[i][0]
        step = trace[i][1]
        if step != 0:
            if dir == 0:
                if (pos[1] + step + 1) > p_matrix.shape[1]:
                    p_matrix = resize(p_matrix, pos[1] + step - p_matrix.shape[1] + 1, 1, dir)
                p_matrix[pos[0], (pos[1] + 1):(pos[1] + step + 1)] = 1
                pos[1] = pos[1] + step
            elif dir == 1:
                if (pos[0] + step + 1) > p_matrix.shape[0]:
                    p_matrix = resize(p_matrix, pos[0] + step - p_matrix.shape[0] + 1, 0, dir)
                p_matrix[(pos[0] + 1):(pos[0] + 1 + step), pos[1]] = 1
                pos[0] = pos[0] + step
            elif dir == 2:
                if (pos[1] - step) < 0:
                    p_matrix = resize(p_matrix, step - pos[1], 1, dir)
                    pos[1] = step
                p_matrix[pos[0], (pos[1] - step):(pos[1])] = 1
                pos[1] = pos[1] - step
            else:
                if (pos[0] - step) < 0:
                    p_matrix = resize(p_matrix, step - pos[0], 0, dir)
                    pos[0] = step
                p_matrix[(pos[0] - step):(pos[0]), pos[1]] = 1
                pos[0] = pos[0] - step
    return p_matrix


def tracing(path):
    dir = 0  # pointing right
    # 0-> direita ; 1-> baixo ; 2-> esquerda ; 3->cima
    trace = []
    for j in range(len(path)):
        step = 0
        if path[j][0] == 0:
            if len(path[j]) == 2:
                step = path[j][1]
            else:
                step = 1
        else:
            if len(path[j]) == 2:
                dir = (((path[j][0] * path[j][1]) + dir) % 4)
            else:
                dir = (dir + path[j][0]) % 4
        trace.append([dir, step])
    return trace


def pathing(code):
    path = []
    way = -1
    num = -1
    for i in range(len(code)):
        if i < num:
            continue
        qnt = ""
        num = i
        if code[i].isdecimal():
            if num < len(code):
                while code[num].isdecimal():
                    qnt += code[num]
                    if num + 1 >= len(code):
                        break
                    num += 1
                if len(path[way]) < 2:
                    length = int(qnt, 10)
                    path[way].append(length)
        else:
            way += 1
            path.append([])
            path[way].append(switch(code[i]))
    return path


def str_mx(matrix):
    str = []
    subm = np.full(matrix.shape, ' ')
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j]:
                subm[i][j] = '*'
        if i > 0:
            str.append("\r\n")
        str.append(''.join(subm[i]))
    return ''.join(str)


def execute(code):
    path = pathing(code)
    trace = tracing(path)
    matrix = mk_matrix(trace)
    print(matrix)
    str = str_mx(matrix)
    return str
