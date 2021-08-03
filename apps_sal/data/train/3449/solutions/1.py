def categorize_study(p_value, requirements):
    p = p_value * 2**(6 - requirements)
    return 'Fine' if p < 0.05 and requirements > 0 else 'Needs review' if p < 0.15 else 'Pants on fire'
