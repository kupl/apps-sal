def pass_the_bill(par, con, ref):
    return -1 if ref >= par / 2 else max(0, par // 2 + 1 - con)
