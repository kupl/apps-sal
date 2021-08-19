dir_dict = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def rpg(field, actions):
    (width, height) = (len(field[0]), len(field))
    (field, actions) = ([list(line) for line in field], list(actions))
    found = False
    for row in range(height):
        if found:
            break
        for col in range(width):
            if field[row][col] in dir_dict:
                player_loc = (row, col)
                player_dir = field[row][col]
                target_loc = (row + dir_dict[player_dir][0], col + dir_dict[player_dir][1])
                found = True
                break
    (hlh, atk, des, bag) = (3, 1, 1, [])
    mer_dict = {}
    (enemy_count, dl_hlh) = (0, 10)
    for action in actions:
        if action not in dir_dict:
            if target_loc[0] < 0 or target_loc[0] >= height or target_loc[1] < 0 or (target_loc[1] >= width):
                return None
            target_tile = field[target_loc[0]][target_loc[1]]
        if action == 'C':
            if target_tile != 'M':
                return None
            if action not in bag:
                return None
            bag.remove(action)
            if target_loc not in mer_dict:
                mer_dict[target_loc] = 2
            else:
                mer_dict[target_loc] = mer_dict[target_loc] - 1
                if mer_dict[target_loc] == 0:
                    field[target_loc[0]][target_loc[1]] = ' '
        elif action == 'K':
            if target_tile not in '-|':
                return None
            if action not in bag:
                return None
            bag.remove(action)
            field[target_loc[0]][target_loc[1]] = ' '
        else:
            if action == 'F':
                if target_tile in ['C', 'K', 'H']:
                    bag.append(target_tile)
                    bag.sort()
                elif target_tile == 'S':
                    des = des + 1
                elif target_tile == 'X':
                    atk = atk + 1
                elif target_tile != ' ':
                    return None
                field[target_loc[0]][target_loc[1]] = player_dir
                field[player_loc[0]][player_loc[1]] = ' '
            elif action in dir_dict:
                player_dir = action
                field[player_loc[0]][player_loc[1]] = action
                target_loc = (player_loc[0] + dir_dict[player_dir][0], player_loc[1] + dir_dict[player_dir][1])
            elif action == 'A':
                if target_tile == 'E':
                    field[target_loc[0]][target_loc[1]] = ' '
                    enemy_count = enemy_count + 1
                    if enemy_count == 3:
                        enemy_count = 0
                        atk = atk + 1
                elif target_tile == 'D':
                    dl_hlh = dl_hlh - atk
                    if dl_hlh <= 0:
                        field[target_loc[0]][target_loc[1]] = ' '
                else:
                    return None
            elif action == 'H':
                if action not in bag:
                    return None
                hlh = 3
                bag.remove(action)
            for d in dir_dict:
                check_loc = (player_loc[0] + dir_dict[d][0], player_loc[1] + dir_dict[d][1])
                if check_loc[0] >= 0 and check_loc[0] < height and (check_loc[1] >= 0) and (check_loc[1] < width):
                    if field[check_loc[0]][check_loc[1]] == 'E':
                        hlh = hlh - max(0, 2 - des)
                    elif field[check_loc[0]][check_loc[1]] == 'D':
                        hlh = hlh - max(0, 3 - des)
                    if hlh <= 0:
                        return None
            if action == 'F':
                player_loc = target_loc
                target_loc = (target_loc[0] + dir_dict[player_dir][0], target_loc[1] + dir_dict[player_dir][1])
    return tuple([field, hlh, atk, des, bag])
