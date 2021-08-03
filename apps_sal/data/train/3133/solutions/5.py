vaccines = {"8 weeks": {"fiveInOne", "pneumococcal", "rotavirus", "meningitisB"},
            "12 weeks": {"fiveInOne", "rotavirus"},
            "16 weeks": {"fiveInOne", "pneumococcal", "meningitisB"},
            "12 months": {"meningitisB", "hibMenC", "measlesMumpsRubella"},
            "40 months": {"measlesMumpsRubella", "preSchoolBooster"},
            "september": {"offer fluVaccine"},
            "october": {"offer fluVaccine"},
            "november": {"offer fluVaccine"}}


def get(x): return vaccines.get(x, set())


def vaccine_list(age, status, month):
    return sorted(get(age) | get(status) | get(month))
