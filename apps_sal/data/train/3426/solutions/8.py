def tax_calculator(total):
    return round((total - 30) * 0.03 + 2.2 if total - 30 > 0 else (total - 20) * 0.05 + 1.7 if total - 20 > 0 else (total - 10) * 0.07 + 1 if total - 10 > 0 else total * 0.1, 2) if (type(total) == int or type(total) == float) and total > 0 else 0
