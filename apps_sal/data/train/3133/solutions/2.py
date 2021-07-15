def vaccine_list(age, status, month):
    vaccines = {
        '8 weeks': {'fiveInOne', 'pneumococcal', 'rotavirus', 'meningitisB'},
        '12 weeks' : {'fiveInOne', 'rotavirus'}, 
        '16 weeks' : {'fiveInOne', 'pneumococcal', 'meningitisB'}, 
        '12 months': {'meningitisB', 'hibMenC','measlesMumpsRubella'},
        '40 months': {'measlesMumpsRubella', 'preSchoolBooster'},
        'up-to-date': set(),
        'september': {'offer fluVaccine'},
        'october': {'offer fluVaccine'},
        'november': {'offer fluVaccine'} }
    return sorted(vaccines[age] | vaccines[status] | vaccines.get(month, set()))
