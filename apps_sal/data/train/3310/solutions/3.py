from collections import OrderedDict

def solve_tie_2(_vaulter_list, names, res, c):
    third_criterion = {}
    for player in _vaulter_list:
        if player["name"] in names:
            fails = ''.join(player["results"]).count("X")
            if fails in third_criterion:
                third_criterion[fails].append(player["name"])
            else:
                third_criterion[fails] = [player["name"]]
    third_criterion = OrderedDict(sorted(third_criterion.items()))
    for pair in third_criterion.items():
        if len(pair[1]) == 1:
            res.append(pair[1][0])
            remove_from_dict(_vaulter_list, res[-1])
            c += 1
            if len(res) >= 3 or c >= 3: return c
        else: # unsolvable tie
            res.append(', '.join(sorted(pair[1])))
            for name in pair[1]:
                remove_from_dict(_vaulter_list, name)
            c += len(pair[1])
            if len(res) >= 3 or c >= 3: return c
    return c

def solve_tie_1(_vaulter_list, names, index, res, c):
    second_criterion = {}
    for player in _vaulter_list:
        if player["name"] in names:
            fails = player["results"][index].count("X")
            if fails in second_criterion:
                second_criterion[fails].append(player["name"])
            else:
                second_criterion[fails] = [player["name"]]
    second_criterion = OrderedDict(sorted(second_criterion.items()))
    for pair in second_criterion.items():
        if len(pair[1]) == 1:
            res.append(pair[1][0])
            remove_from_dict(_vaulter_list, res[-1])
            c += 1
            if len(res) >= 3 or c >= 3: return c
        else: # try to solve according to next criterion
            c = solve_tie_2(_vaulter_list, pair[1], res, c)
            if len(res) >= 3: return c
    return c

def remove_from_dict(_vaulter_list, name):
    for i in range(len(_vaulter_list)):
        if _vaulter_list[i]["name"] == name:
            del _vaulter_list[i]
            break

def score_pole_vault(vaulter_list):
    if len(vaulter_list) < 1: return {}
    _vaulter_list = vaulter_list.copy()
    res = []
    c = 0
    l = len(_vaulter_list[0]["results"])
    best_height_index = l
    while len(res) < 3 and c < 3:
        for i in range(l-1, -1, -1):
            for player in _vaulter_list:
                if "O" in player["results"][i]:
                    best_height_index = i
                    break
            if best_height_index < l: # found
                break
        first_criterion_players = []
        for player in _vaulter_list:
            if "O" in player["results"][best_height_index]:
                first_criterion_players.append(player["name"])
        if len(first_criterion_players) == 1:
            res.append(first_criterion_players[0])
            remove_from_dict(_vaulter_list, res[-1])
            c += 1
        else:
            c = solve_tie_1(_vaulter_list, first_criterion_players, best_height_index, res, c)
        l = best_height_index
    
    res_dict = {"1st": res[0] + (" (jump-off)" if "," in res[0] else "")}
    n = len(res_dict["1st"].split(","))
    if n == 3: return res_dict
    if n == 2:
        res_dict["3rd"] = res[1] + (" (tie)" if "," in res[1] else "")
        return res_dict
    else:
        res_dict["2nd"] = res[1] + (" (tie)" if "," in res[1] else "")
        if "," in res_dict["2nd"]: return res_dict
        else:
            res_dict["3rd"] = res[2] + (" (tie)" if "," in res[2] else "")
            return res_dict
