vaccinations = {'8 weeks': {'fiveInOne', 'pneumococcal', 'rotavirus', 'meningitisB'}, '12 weeks': {'fiveInOne', 'rotavirus'}, '16 weeks': {'fiveInOne', 'pneumococcal', 'meningitisB'}, '12 months': {'meningitisB', 'hibMenC', 'measlesMumpsRubella'}, '40 months': {'measlesMumpsRubella', 'preSchoolBooster'}, 'september': {'offer fluVaccine'}, 'october': {'offer fluVaccine'}, 'november': {'offer fluVaccine'}}


def vaccine_list(age, status, month):
    return sorted(vaccinations[age] | vaccinations.get(status, set()) | vaccinations.get(month, set()))
