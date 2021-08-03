def check_valid_tr_number(n):
    if not isinstance(n, int) or not 9999999999 < n < 100000000000:
        return False
    dig = [int(d) for d in str(n)]
    return (sum(dig[:9:2]) * 7 - sum(dig[1:9:2])) % 10 == dig[9] and sum(dig[:10]) % 10 == dig[10]
