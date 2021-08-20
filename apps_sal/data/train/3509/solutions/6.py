from decimal import Context, ROUND_HALF_UP
import re


def meters(num):
    r = len(str(num).strip('0'))
    num = Context(prec=r, rounding=ROUND_HALF_UP).create_decimal(num)
    i = int(num.logb()) // 3
    return re.sub('(\\.0+)(?=[kMGTPEZTY])', '', f"{num.scaleb(-3 * i):f}{' kMGTPEZY'[i]}m".replace(' ', ''))
