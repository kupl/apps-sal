from itertools import chain

def vaccine_list(age, status, month): 
    flu_months = ['september','october','november'] 
    vac_sched = {'8 weeks': ['fiveInOne', 'pneumococcal', 'rotavirus', 'meningitisB'],
                   '12 weeks': ['fiveInOne', 'rotavirus'],
                   '16 weeks': ['fiveInOne', 'pneumococcal', 'meningitisB'],
                   '12 months': ['meningitisB', 'hibMenC', 'measlesMumpsRubella'],
                   '40 months': ['measlesMumpsRubella', 'preSchoolBooster']} 
    
    if status == 'up-to-date':
              status = age

    vac_time = list(vac_sched.keys())
    vacs_toDo = [v for k,v in vac_sched.items() if k in [status, age]]

    vac_list = list(set(list(chain.from_iterable(vacs_toDo))))
       
    if month in flu_months:
              vac_list.append('offer fluVaccine')

    return sorted(vac_list)
