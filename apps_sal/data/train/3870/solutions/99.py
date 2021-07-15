def solve(s):
    rev_s = ''.join(s.replace(' ', '')[::-1])
    result = ''
    for i in s.split():
        result += rev_s[: len(i)] + ' '
        rev_s = rev_s[len(i):]
    result = result.strip()
    return result + ' ' if len(s) != len(result) else result
