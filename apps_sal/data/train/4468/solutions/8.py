def simplify(n):
    s = str(n)
    l = len(s)
    result = []
    for i, d in enumerate(s, 1):
        if int(d):
            p = "" if l == i else f"*{10**(l-i)}"
            result.append(f"{d}{p}")
    return "+".join(result)
