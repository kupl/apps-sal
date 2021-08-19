def simplify(n):
    s = str(n)
    l = len(s)
    result = []
    for i, d in enumerate(s, 1):
        if int(d):
            p = "" if l == i else f"*{10**(l-i)}"
            result.append(f"{d}{p}")
    return "+".join(result)


#    s = str(n)
#    return  "+".join(f"{d}{f'*{10**(-i)}' if i else ''}" for i, d in enumerate(s, -len(s)+1) if int(d))
