def categorize_study(p_value, requirements):
    bs_factor = 2**(6-requirements)
    product = p_value * bs_factor
    
    if 0.0 < product < .05:
        result = 'Fine'
    elif 0.05 < product <0.15:
        result = 'Needs review'
    else:
        result = 'Pants on fire'
    
    if requirements == 0 and result == 'Fine':
        result = 'Needs review'
    return result

