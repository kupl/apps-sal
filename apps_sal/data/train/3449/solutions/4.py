def categorize_study(p_value, requirements):
    bsfactors = [64, 32, 16, 8, 4, 2, 1]
    score = p_value * bsfactors[requirements]
    if score < 0.05:
        if requirements > 1:
            return 'Fine'
        if requirements == 0:
            return 'Needs review'
    if 0.05 < score < 0.15:
        return 'Needs review'
    if score >= 0.015:
        return 'Pants on fire'
