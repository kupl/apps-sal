from decimal import Decimal


def p_num(n):
    return ((24 * Decimal(n) + 1) ** Decimal(0.5) + 1) / 6 % 1 < 1e-16


def g_p_num(n):
    return (24 * Decimal(n) + 1) ** Decimal(0.5) % 1 < 1e-16


def s_p_num(n):
    return Decimal(n) ** Decimal(0.5) % 1 < 1e-16 and p_num(n)
