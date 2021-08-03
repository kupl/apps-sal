def rain_amount(mm):
    if mm < 40:
        a = "You need to give your plant "
        b = "mm of water"
        s = ""
        s += a
        st = 40 - mm
        st = str(st)
        s += st
        s += b
        return s
    else:
        return "Your plant has had more than enough water for today!"
