def balanced_num(n):
    rs = list(map(int, str(n)))
    if len(rs) == 1 or len(rs) == 2:
        return 'Balanced'
    else:
        if len(rs) % 2 == 0 and len(rs) > 2:
            if sum(rs[:int(len(rs) / 2) - 1]) == sum(rs[-(int(len(rs) / 2) - 1):]):
                return 'Balanced'
            else:
                return 'Not Balanced'
        else:
            if sum(rs[:int(len(rs) / 2)]) == sum(rs[-(int(len(rs) / 2)):]):
                return 'Balanced'
            else:
                return 'Not Balanced'
