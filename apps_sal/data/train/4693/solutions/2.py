def check_valid_tr_number(number):
    s = str(number)
    return (
        len(s) == 11
        and s.isdigit()
        and not s.startswith('0')
        and (sum(map(int, s[:9:2])) * 7 - sum(map(int, s[1:8:2]))) % 10 == int(s) // 10 % 10
        and sum(map(int, s[:10])) % 10 == int(s) % 10
    )
