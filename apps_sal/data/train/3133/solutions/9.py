def vaccine_list(age, status, month):

    dict = {'fiveInOne': ['8 weeks', '12 weeks', '16 weeks'], 'pneumococcal': ['8 weeks', '16 weeks'],
            'rotavirus': ['8 weeks', '12 weeks'], 'meningitisB': ['8 weeks', '16 weeks', '12 months'],
            'hibMenC': ['12 months'], 'measlesMumpsRubella': ['12 months', '40 months'],
            'fluVaccine': ['september', 'october', 'november'], 'preSchoolBooster': ['40 months']}

    vac_list = []
    for key in dict:
        if age in dict[key] or status in dict[key]:
            vac_list.append(key)

    if month in dict['fluVaccine']:
        vac_list.append('offer fluVaccine')

    return sorted(vac_list)
