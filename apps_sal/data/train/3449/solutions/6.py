def categorize_study(p_value, requirements):
    prod = p_value * (1 << 6 - requirements)
    return 'Pants on fire' if prod >= 0.15 else 'Needs review' if requirements == 0 or prod >= 0.05 else 'Fine'
