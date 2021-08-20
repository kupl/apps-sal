def communication_module(s):
    result = str(max(0, min(int(s[8:12]) + int(s[12:16]) if s[4] == '0' else int(s[8:12]) - int(s[12:16]) if s[4] == 'B' else int(s[8:12]) * int(s[12:16]), 9999)))
    return s[:4] + 'FFFF' + '0' * (4 - len(result)) + result + '0000' + s[-4:]
