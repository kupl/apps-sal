from decimal import Decimal
p_num = lambda n: ((24 * Decimal(n) + 1) ** Decimal(.5) + 1) / 6 % 1 < 0.0000000000000001
g_p_num = lambda n: (24 * Decimal(n) + 1) ** Decimal(.5) % 1 < 0.0000000000000001
s_p_num = lambda n: Decimal(n) ** Decimal(.5) % 1 < 0.0000000000000001 and p_num(n)
