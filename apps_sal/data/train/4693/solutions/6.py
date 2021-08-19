def check_valid_tr_number(number):
    n = str(number)
    return isinstance(number, int) and len(n) == 11 and (str((sum((int(n[i]) for i in range(0, 10, 2))) * 7 - sum((int(n[i]) for i in range(1, 8, 2)))) % 10) == n[9]) and (str(sum((int(n[i]) for i in range(10))) % 10) == n[10])
