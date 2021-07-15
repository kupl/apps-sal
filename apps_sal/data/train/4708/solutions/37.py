from typing import List

def human_years_cat_years_dog_years(human_years: int) -> List[int]:
    """ Get respective ages for human, cats, dogs. """
    __get_animals_years_multiplier = lambda _def: [{1: 15, 2: 9}.get(_it, _def) for _it in list(range(1, human_years + 1))]
    return [
        human_years,
        sum(__get_animals_years_multiplier(4)),
        sum(__get_animals_years_multiplier(5)),
    ]
