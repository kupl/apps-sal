def starts_with(st, prefix):
    if len(st) == 0 != len(prefix):
        return False
    elif len(prefix) == 0:
        return True
    else:
        try:
            a = 0
            for i in range(len(prefix)):
                if st[i] == prefix[i]:
                    a += 1
            if a == len(prefix):
                return True
            else:
                return False
        except:
            return False
