def remove(s):
    tmp = s.split(" ")
    for i,x in enumerate(tmp):
        before = 0
        after = 0
        while x[0] == "!":
            before += 1
            x = x[1:]
        while x[-1] == "!":
            after += 1
            x = x[:-1]
        count = min(before,after)
        bangs = "!" * count
        tmp[i] = bangs + x + bangs
    return " ".join(tmp)
        
            

