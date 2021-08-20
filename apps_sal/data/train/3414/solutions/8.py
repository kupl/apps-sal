import re


def reversi_row(moves):
    res = '.' * 8
    star = False
    for move in moves:
        star = not star
        assert res[move] == '.'
        res = res[:move] + '@' + res[move + 1:]
        if star:
            res = re.sub('(@)(O+)(\\*)', lambda g: g[1] + '*' * len(g[2]) + g[3], res)
            res = re.sub('(\\*)(O+)(@)', lambda g: g[1] + '*' * len(g[2]) + g[3], res)
            res = res.replace('@', '*')
        else:
            res = re.sub('(@)(\\*+)(O)', lambda g: g[1] + 'O' * len(g[2]) + g[3], res)
            res = re.sub('(O)(\\*+)(@)', lambda g: g[1] + 'O' * len(g[2]) + g[3], res)
            res = res.replace('@', 'O')
    return res
