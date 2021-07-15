def string_clean(s):
    num = "0123456789"
    fresh = []
    
    for i in s:
        if i not in num:
            fresh.append(i)
    return "".join(fresh)
