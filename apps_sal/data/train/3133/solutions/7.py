vaccines = {'8 weeks': ['fiveInOne', 'pneumococcal', 'rotavirus', 'meningitisB'], '12 weeks': ['fiveInOne', 'rotavirus'], '16 weeks': ['fiveInOne', 'pneumococcal', 'meningitisB'], '12 months': ['meningitisB', 'measlesMumpsRubella', 'hibMenC'], '40 months': ['measlesMumpsRubella', 'preSchoolBooster'], 'september': ['offer fluVaccine'], 'october': ['offer fluVaccine'], 'november': ['offer fluVaccine']}


def vaccine_list(age, status, month):
    lists_of_vaccines = [vaccines[v] for v in [age, status, month] if v in vaccines]
    return sorted(list(set([v for lst in lists_of_vaccines for v in lst])))
