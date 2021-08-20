VACCINATIONS = {'fiveInOne': ['8 weeks', '12 weeks', '16 weeks'], 'pneumococcal': ['8 weeks', '16 weeks'], 'rotavirus': ['8 weeks', '12 weeks'], 'meningitisB': ['8 weeks', '16 weeks', '12 months'], 'hibMenC': ['12 months'], 'measlesMumpsRubella': ['12 months', '40 months'], 'preSchoolBooster': ['40 months']}


def vaccine_list(age, status, month):
    return sorted(({'offer fluVaccine'} if month in ['september', 'october', 'november'] else set()) | {v for (v, times) in VACCINATIONS.items() if age in times or (status != 'up-to-date' and status in times)})
