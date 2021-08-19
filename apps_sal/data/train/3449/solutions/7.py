def categorize_study(p_value, requirements):
    bs_factor = 2 ** (6 - requirements)
    if bs_factor * p_value < 0.05 and requirements > 0:
        return 'Fine'
    elif bs_factor * p_value > 0.15:
        return 'Pants on fire'
    else:
        return 'Needs review'
