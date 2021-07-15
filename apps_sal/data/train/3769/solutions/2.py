import re

def execute(code):
    if code == '':
        return '*'
    turn_right = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    turn_left =  [[-1, 0], [0, -1], [1, 0], [0, 1]]
    path = re.findall('F\d+|F|L\d+|L|R\d+|R', code)
    max_size = sum([1 if j == 'F' else int(j[1:]) for j in path if 'F' in j]) * 2
    table = [[' '] * (max_size + 1) for i in range(max_size + 1)]
    x, y = max_size // 2, max_size // 2
    table[x][y] = '*'
    f1, f2 = 0, 1
    for way in path:
        if 'R' in way:
            for i in range(1 if way == 'R' else int(way[1:])):
                cur_pos = [pos for pos, coords in enumerate(turn_right) if coords == [f1, f2]][0]
                f1, f2 = turn_right[0] if cur_pos == 3 else turn_right[cur_pos + 1]
        if 'L' in way:
            for i in range(1 if way == 'L' else int(way[1:])):
                cur_pos = [pos for pos, coords in enumerate(turn_left) if coords == [f1, f2]][0]
                f1, f2 = turn_left[0] if cur_pos == 3 else turn_left[cur_pos + 1]        
        if 'F' in way:
            for i in range(1 if way == 'F' else int(way[1:])):
                x += 1 * f1
                y += 1 * f2
                table[x][y] = '*'
    solution = [i for i in table if '*' in i]
    solution = [i for i in zip(*solution[:]) if '*' in i]
    for i in range(3):
        solution = list(zip(*solution[:]))
    final_way = [''.join([j for j in i]) for i in solution]
    return '\r\n'.join(final_way)
