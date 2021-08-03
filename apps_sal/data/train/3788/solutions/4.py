from decimal import Decimal
def p_num(n): return (lambda deltasq: ((1 + deltasq) / 6) % 1 == 0)(Decimal(1 + 24 * n).sqrt())
def g_p_num(n): return (lambda deltasq: ((1 + deltasq) / 6) % 1 == 0 or ((1 - deltasq) / 6) % 1 == 0)(Decimal(1 + 24 * n).sqrt())
def s_p_num(n): return p_num(n) and Decimal(n).sqrt() % 1 == 0
