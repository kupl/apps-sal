from decimal import Decimal
def p_num(n): return ((24 * Decimal(n) + 1) ** Decimal(.5) + 1) / 6 % 1 < 0.0000000000000001
def g_p_num(n): return (24 * Decimal(n) + 1) ** Decimal(.5) % 1 < 0.0000000000000001
def s_p_num(n): return Decimal(n) ** Decimal(.5) % 1 < 0.0000000000000001 and p_num(n)
