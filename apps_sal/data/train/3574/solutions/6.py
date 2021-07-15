def Dragon(n):
    if type(n) != int or n < 0:
        return ""
    stg, a, b = "F{a}", "{a}R{b}FR", "LF{a}L{b}"
    for _ in range(n):
        stg = stg.format(a=a, b=b)
    return stg.replace("{a}", "").replace("{b}", "")
