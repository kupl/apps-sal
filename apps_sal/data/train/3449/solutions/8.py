def categorize_study(p_value, requirements):
    rate = p_value * 2 ** (6 - requirements)
    if rate < 0.05:
        if requirements != 0:
            return 'Fine'
        else:
            return 'Needs review'
    elif rate >= 0.05 and rate < 0.15:
        return 'Needs review'
    else:
        return 'Pants on fire'
