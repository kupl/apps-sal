def categorize_study(p_value, requirements):
    bs_factor = 2 ** (6 - requirements)
    product = p_value * bs_factor
    if product >= 0.15:
        return 'Pants on fire'
    elif 0.05 <= product < 0.15 or requirements == 0:
        return 'Needs review'
    else:
        return 'Fine'
