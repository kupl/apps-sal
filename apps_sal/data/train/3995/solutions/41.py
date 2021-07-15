def dating_range(age):
    return f'{int(age-age*.10)}-{int(age+age*.10)}' if age <= 14 else f'{age//2+7}-{(age-7)*2}'
