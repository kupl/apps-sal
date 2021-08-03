from itertools import chain

TOME = {
    '8 weeks': ['fiveInOne', 'pneumococcal', 'rotavirus', 'meningitisB'],
    '12 weeks': ['fiveInOne', 'rotavirus'],
    '16 weeks': ['fiveInOne', 'pneumococcal', 'meningitisB'],
    '12 months': ['meningitisB', 'hibMenC', 'measlesMumpsRubella'],
    '40 months': ['measlesMumpsRubella', 'preSchoolBooster'],
    'september': ['offer fluVaccine'],
    'october': ['offer fluVaccine'],
    'november': ['offer fluVaccine'],
}


def vaccine_list(*args):
    return sorted(set(chain.from_iterable(
        TOME.get(s, ()) for s in args
    )))
