def vaccine_list(age, status, month):
    vaccine = {'fiveInOne': ['8 weeks', '12 weeks', '16 weeks'], 'pneumococcal': ['8 weeks', '16 weeks'], 'rotavirus': ['8 weeks', '12 weeks'], 'meningitisB': ['8 weeks', '16 weeks', '12 months'], 'hibMenC': ['12 months'], 'measlesMumpsRubella': ['12 months', '40 months'], 'fluVaccine': ['september', 'october', 'november'], 'preSchoolBooster': ['40 months']}
    req = []
    for jab in vaccine:
        if status in vaccine[jab]:
            req.append(jab)
        if age in vaccine[jab] and jab not in req:
            req.append(jab)
    if month in vaccine['fluVaccine']:
        req.append('offer fluVaccine')
    req.sort()
    return req
