d = {'fiveInOne': ('8 weeks', '12 weeks', '16 weeks'),
     'pneumococcal': ('8 weeks', '16 weeks'),
     'rotavirus': ('8 weeks', '12 weeks'),
     'meningitisB': ('8 weeks', '16 weeks', '12 months'),
     'hibMenC': ('12 months',),
     'measlesMumpsRubella': ('12 months', '40 months'),
     'offer fluVaccine': ('september', 'october', 'november'),
     'preSchoolBooster': ('40 months',)}
vaccine_list = lambda *args: sorted({k for i in args for k, l in d.items() if i in l if i != 'up-to-date'})
