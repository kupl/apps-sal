def denumerate(enum_list):
    try:
        # tuple validation
        for t in enum_list:
            if ((len(t) != 2) or
                (not t[1].isalnum()) or
                (len(t[1]) != 1)):
                return False
        
        a,b = zip(*sorted(enum_list))
        
        if list(a) == list(range(len(a))):
            return "".join(b)
        else:
            return False
    except:
        return False
