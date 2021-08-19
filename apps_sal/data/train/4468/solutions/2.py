def simplify(n):
    n = str(n)
    return "".join(["+" + n[i] + ("*1" + "0" * (len(n) - i - 1) if len(n) - i - 1 > 0 else "") for i in range(0, len(n)) if n[i] != "0"])[1:]
    # . . . :D
