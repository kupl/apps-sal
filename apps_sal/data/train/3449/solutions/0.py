def categorize_study(p_value, requirements):
    study_value = p_value * (2**(6 - requirements))

    if study_value < 0.05 and requirements != 0:
        return "Fine"
    elif study_value < 0.05 and requirements == 0:
        return "Needs review"
    elif study_value > 0.05 and study_value < 0.15:
        return "Needs review"
    else:
        return "Pants on fire"
