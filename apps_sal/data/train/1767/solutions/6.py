from collections import Counter


def solution(tiles):
    print(tiles)
    cnts = {}
    for i in range(1, 10):
        if str(i) in tiles:
            cnts[i] = tiles.count(str(i))
        else:
            cnts[i] = 0
    print(cnts)
    res = ''
    for i in range(1, 10):
        winset = []
        if cnts[i] < 4:
            cnts[i] += 1
            if win(cnts, 0, winset):
                res += str(i)
            cnts[i] -= 1
    return res


def win(cnts, pair, winset):
    if sum(cnts.values()) == 0:
        return True
    seqdic = {1: [(2, 3)], 2: [(1, 3), (3, 4)], 3: [(1, 2), (2, 4), (4, 5)], 4: [(2, 3), (3, 5), (5, 6)], 5: [(3, 4), (4, 6), (6, 7)], 6: [(4, 5), (5, 7), (7, 8)], 7: [(5, 6), (5, 8), (8, 9)], 8: [(6, 7), (7, 9)], 9: [(7, 8)]}
    tiles = [i for i in cnts.keys() if cnts[i] > 0]
    i = tiles[0]
    if cnts[i] == 1:
        for j in seqdic[i]:
            if cnts[j[0]] > 0 and cnts[j[1]] > 0:
                cnts_c = cnts.copy()
                cnts_c[j[0]] -= 1
                cnts_c[j[1]] -= 1
                cnts_c[i] -= 1
                if win(cnts_c, pair, winset):
                    winset.append((j[0], j[1], i))
                    return True
        return False
    if cnts[i] == 2:
        if not pair:
            cnts_c = cnts.copy()
            cnts_c[i] -= 2
            if win(cnts_c, 1, winset):
                winset.append((i, i))
                return True
        for j in seqdic[i]:
            if cnts[j[0]] > 1 and cnts[j[1]] > 1:
                cnts_c = cnts.copy()
                cnts_c[j[0]] -= 2
                cnts_c[j[1]] -= 2
                cnts_c[i] -= 2
                if win(cnts_c, pair, winset):
                    winset += [(j[0], j[1], i)] * 2
                    return True
        return False
    if cnts[i] == 3:
        if not pair:
            cnts_c = cnts.copy()
            cnts_c[i] -= 2
            if win(cnts_c, 1, winset):
                winset.append((i, i))
                return True
        cnts_c = cnts.copy()
        cnts_c[i] -= 3
        if win(cnts_c, pair, winset):
            winset.append((i, i, i))
            return True
        for j in seqdic[i]:
            if cnts[j[0]] > 2 and cnts[j[1]] > 2:
                cnts_c = cnts.copy()
                cnts_c[j[0]] -= 3
                cnts_c[j[1]] -= 3
                cnts_c[i] -= 3
                if win(cnts_c, pair, winset):
                    winset += [(j[0], j[1], i)] * 3
                    return True
        return False
    if cnts[i] == 4:
        if not pair:
            cnts_c = cnts.copy()
            cnts_c[i] -= 2
            if win(cnts_c, 1, winset):
                winset.append((i, i))
                return True
        cnts_c = cnts.copy()
        cnts_c[i] -= 3
        if win(cnts_c, pair, winset):
            winset.append((i, i, i))
            return True
        for j in seqdic[i]:
            if cnts[j[0]] > 3 and cnts[j[1]] > 3:
                cnts_c = cnts.copy()
                cnts_c[j[0]] -= 4
                cnts_c[j[1]] -= 4
                cnts_c[i] -= 4
                if win(cnts_c, pair, winset):
                    winset += [(j[0], j[1], i)] * 4
                    return True
        return False
