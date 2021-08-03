def balanced_num(number):
    stg = str(number)
    half = (len(stg) - 1) // 2
    diff = sum(int(stg[i]) - int(stg[-1 - i]) for i in range(half))
    return "Not Balanced" if diff else "Balanced"
