def convert_to_mixed_numeral(parm):
    num, den = map(int, parm.split("/"))
    sign, num = num < 0,  abs(num)
    
    if num < den:
        return parm
    
    whole, num = divmod(num, den)
    if num == 0:
        return "-"*sign + "%d" % whole
    return "-"*sign + "%d %d/%d" % (whole, num, den)
