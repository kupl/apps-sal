# 需要考虑保留一位小数，采用round(a,1)的方法，计算部分十分简单。
def nba_extrap(ppg, mpg):
    if mpg != 0:
        ppg = (ppg/mpg)*48
        return round(ppg,1)
