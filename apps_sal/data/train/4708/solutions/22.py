from functools import partial

infinity = float('inf')


def human_years_cat_years_dog_years(human_years):
    age = Age.from_human(human_years)
    return [age.as_human, age.as_cat, age.as_dog]


class AgeConversionsMeta(type):

    def __new__(meta, name, bases, namespace):
        attr_name = namespace.pop('_attr_name_', 'normalized_age')
        conversions = namespace.pop('_conversions_', {})
        if conversions:
            def as_(self, year_to_multiplier):
                age = getattr(self, attr_name)
                converted_age = previous_year = 0
                for year, multiplier in year_to_multiplier:
                    is_older = age > year
                    years_difference = (year if is_older else age) - previous_year
                    converted_age += multiplier * years_difference
                    if not is_older:
                        break
                    previous_year = year
                return converted_age

            for name, year_to_multiplier in conversions.items():
                namespace['from_' + name] = classmethod(partial(meta.__from, year_to_multiplier=year_to_multiplier))
                namespace['as_' + name] = property(partial(as_, year_to_multiplier=year_to_multiplier))

        def __init__(self, normalized_age):
            setattr(self, attr_name, normalized_age)
        namespace['__init__'] = __init__

        return super().__new__(meta, name, bases, namespace)

    def __from(cls, age, year_to_multiplier):
        normalized_age = previous_year = 0
        for year, multiplier in year_to_multiplier:
            years_difference = year - previous_year
            max_age_in_range = multiplier * years_difference
            if age <= max_age_in_range:
                normalized_age += age / multiplier
                break
            age -= max_age_in_range
            previous_year = year
            normalized_age += years_difference
        return cls(normalized_age)


class Age(metaclass=AgeConversionsMeta):
    _conversions_ = {
        'human': ((infinity, 1),),
        'cat': (
            (1, 15),
            (2, 9),
            (infinity, 4)),
        'dog': (
            (1, 15),
            (2, 9),
            (infinity, 5))
    }
