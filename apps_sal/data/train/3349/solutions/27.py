def find_missing_number(s):
    if s =="":
        return 0
    try: s=set(map(int,s.split(" ")))
    except ValueError: return 1
    try: return min(set(range(1,max(s))).difference(s))
    except ValueError: return 0
