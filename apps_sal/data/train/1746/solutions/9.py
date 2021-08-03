only_show_wrong()
playerDirections = {
    "^": (0, -1),
    "<": (-1, 0),
    ">": (1, 0),
    "v": (0, 1)
}
items = ("X", "K", "H", "S", "C")


def rpg(field: List[List[str]], actions: List[str]) -> Tuple[List[List[str]], int, int, int, List[str]]:
    player = {
        "x": 0,
        "y": 0,
        "direction": (0, 0),
        "char": "",
        "health": 3,
        "attack": 1,
        "defense": 1,
        "inventory": [],
        "levelCounter": 0,
        "coinsCounter": 0
    }
    demonLord = 10

    for y, str in enumerate(field):
        for x, char in enumerate(str):
            if char in playerDirections:
                player["x"] = x
                player["y"] = y
                player["direction"] = playerDirections[char]
                player["char"] = char
                break
        else:
            continue
        break

    for action in actions:
        if action in playerDirections:
            player["direction"] = playerDirections[action]
            player["char"] = action

        elif action == "F":
            enemiesClose = []
            for dir in playerDirections.values():
                adjacent = ""
                try:
                    positions = (max(0, player["y"] + dir[1]), max(0, player["x"] + dir[0]))
                    adjacent = field[positions[0]][positions[1]]
                except:
                    adjacent = ""
                if adjacent == "E" or adjacent == "D":
                    player["health"] -= max(0, (2 if adjacent == "E" else 3) - player["defense"])

            field[player["y"]][player["x"]] = " "
            player["x"] += player["direction"][0]
            player["y"] += player["direction"][1]

            if(player["x"] < 0 or player["y"] < 0 or
               player["y"] >= len(field) or player["x"] >= len(field[player["y"]])):
                return None
            nextTile = field[player["y"]][player["x"]]
            if(not nextTile in items and nextTile != " "):
                return None
            if(nextTile in items):
                if nextTile == "X":
                    player["attack"] += 1
                elif nextTile == "S":
                    player["defense"] += 1
                else:
                    player["inventory"].append(nextTile)

        elif action in player["inventory"]:
            if action == "H":
                if player["health"] < 3:
                    player["health"] = 3
                else:
                    return None
            elif action == "K":
                nextTilePos = (player["y"] + player["direction"][1], player["x"] + player["direction"][0])
                if(nextTilePos[1] < 0 or nextTilePos[0] < 0 or
                   nextTilePos[0] >= len(field) or nextTilePos[1] >= len(field[nextTilePos[0]])):
                    return None
                nextTile = field[nextTilePos[0]][nextTilePos[1]]
                if(nextTile == "-" or nextTile == "|"):
                    field[nextTilePos[0]][nextTilePos[1]] = " "
                else:
                    return None
            else:
                nextTilePos = (player["y"] + player["direction"][1], player["x"] + player["direction"][0])
                if(nextTilePos[1] < 0 or nextTilePos[0] < 0 or
                   nextTilePos[0] >= len(field) or nextTilePos[1] >= len(field[nextTilePos[0]])):
                    return None
                if field[nextTilePos[0]][nextTilePos[1]] == "M":
                    player["coinsCounter"] += 1
                    if player["coinsCounter"] >= 3:
                        field[nextTilePos[0]][nextTilePos[1]] = " "
                else:
                    return None
            player["inventory"].remove(action)

        elif action == "A":
            nextTilePos = (player["y"] + player["direction"][1], player["x"] + player["direction"][0])
            nextTile = field[nextTilePos[0]][nextTilePos[1]]
            if nextTile == "E":
                field[nextTilePos[0]][nextTilePos[1]] = " "
                player["levelCounter"] += 1
                if player["levelCounter"] >= 3:
                    player["levelCounter"] = 0
                    player["attack"] += 1
            elif nextTile == "D":
                demonLord -= player["attack"]
                if demonLord <= 0:
                    field[nextTilePos[0]][nextTilePos[1]] = " "
            else:
                return None

        else:
            return None

        if action == "A" or action == "H" or action in playerDirections:
            for dir in playerDirections.values():
                adjacent = ""
                try:
                    positions = (max(0, player["y"] + dir[1]), max(0, player["x"] + dir[0]))
                    adjacent = field[positions[0]][positions[1]]
                except:
                    adjacent = "X"
                if adjacent == "E" or adjacent == "D":
                    player["health"] -= max(0, (2 if adjacent == "E" else 3) - player["defense"])

        if player["health"] <= 0:
            return None

    field[player["y"]][player["x"]] = player["char"]
    return (field, player["health"], player["attack"], player["defense"], sorted(player["inventory"]))
