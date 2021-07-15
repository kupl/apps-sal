def find_missing(a, b):
    for i in a:
        try: b.remove(i)
        except: return i
