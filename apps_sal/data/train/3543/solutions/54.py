def increment_string(s):
    for i in range(5,0,-1):
        if len(s) > i-1 and s[-i].isdigit():
            return s[:-i] + str(int(s[-i:])+1).zfill(i) 
    return s+'1'
