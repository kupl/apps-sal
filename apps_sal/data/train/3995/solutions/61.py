def dating_range(age):
    if age > 14:
        return f'{(age)//2 +7}-{2*(age-7)}'
    else:
        return f'{int(age-age/10)}-{int(age+age/10)}'
