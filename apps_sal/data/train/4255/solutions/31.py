def make_upper_case(s):
    # Code here
    str=""
    for i in s:
        if 97<=ord(i)<=122:
            str=str+chr(ord(i)-32)
        else:
            str=str+i
    return str
