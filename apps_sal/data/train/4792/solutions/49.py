def parse_float(string):
    flag = False
    for ch in string:
        if(((ord(ch) >= ord('0')) and (ord(ch) <= ord('9'))) or (ord(ch) == ord('.'))):
            flag = True
        else:
            flag = False
            break
    if(flag):
        return float("".join(string))
    else:
        return None
