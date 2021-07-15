def increment_string(s):
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))
    
    return s + "1"
