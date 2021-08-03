def dating_range(age):
    return f'{age//2+7}-{(age-7)*2}' if age >= 14 else f'{int(age-0.10*age)}-{int(age+0.10*age)}'
