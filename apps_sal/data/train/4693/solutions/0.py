def check_valid_tr_number(n):
    return type(n) == int and len(str(n)) == 11 and (8 * sum(map(int, str(n)[:-1:2])) % 10 == sum(map(int, str(n)[:-1])) % 10 == n % 10)
