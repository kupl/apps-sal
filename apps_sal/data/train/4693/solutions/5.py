def check_valid_tr_number(number):
    if not isinstance(number, int): return False
    s = str(number)
    if len(s) != 11: return False
    if sum(map(int, s[:-1])) % 10 != int(s[-1]): return False
    if (7*sum(map(int, s[:-1:2])) - sum(map(int, s[1:-2:2]))) % 10 != int(s[-2]): return False
    return True
