def categorize_study(p_value, requirements):
    val = p_value * 2 **(6-requirements)
    return ["Fine" if requirements else "Needs review", 
            "Needs review", 
            "Pants on fire"][ (val > 0.05) + (val > 0.15) ]
