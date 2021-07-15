def string_to_number(s):
    ch = 0
    for i in s:
        if i.isdigit():
            ch = ch * 10 + int(i)
    return ch if s[0] != '-' else -ch
