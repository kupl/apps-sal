def sum_str(a, b):
    try:
        return str(sum([int(a), int(b)]))
    except:
        try:
            return str(int(a))
        except:
            try:
                return str(int(b))
            except:
                return '0'
