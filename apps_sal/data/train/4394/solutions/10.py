def men_still_standing(cards):
    players = [11,11]
    dic = {}
    for string in cards:
        player = string[:-1]
        if player in dic:
            if dic[player][1] != 'out':
                dic[player][0] = 1
        else:
            if string[len(string) - 1] == 'Y':
                dic[player] = [0,'in']
            else:
                dic[player] = [1,'in']
        if dic[player][0] == 1 and dic[player][1] is 'in':
            if player[0] == 'A':
                players[0] -= 1
            else:
                players[1] -= 1
            dic[player][1] = 'out'
        if players[0] < 7 or players[1] < 7:
            return tuple(players)
    return tuple(players)

